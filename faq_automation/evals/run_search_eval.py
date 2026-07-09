"""
Search/retrieval eval for the FAQ merge agent.

Two complementary measurements:

  1. positive eval (recall for DUPLICATE detection):
The target doc is IN the index. Can search find it?
     Metrics: recall@k, MRR@k.

  2. negative eval (false-positive rate for NEW discrimination):
     The target doc is REMOVED from the index (simulating the "before" state
     when the proposal was genuinely new). What does search return?
     If the top results are strong same-topic matches, the agent would wrongly
     call DUPLICATE. We measure this as the false-positive rate at various score
     thresholds.

## The evaluation challenge

Most proposals that the bot processes are NEW — the relevant doc doesn't exist
yet. For those queries, the search is NOT expected to return a relevant doc;
returning nothing useful is the correct outcome. Traditional IR metrics
(recall) assume every query has at least one relevant doc, which
isn't the case here.

We solve this by splitting the eval into two passes (positive and negative) that
each have a clear ground truth, rather than mixing them into one metric:

  - positive: the relevant doc IS in the index. Recall@k = "did we find it?"
  - negative: the relevant doc is NOT in the index. The question is whether the
    search returns a false positive strong enough to mislead the LLM.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.run_search_eval
"""

import os as _os
from pathlib import Path as _Path

def _load_env():
    for candidate in [_Path(__file__).resolve().parents[3], _Path.cwd()]:
        env_file = candidate / '.env'
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, val = line.partition('=')
                if key not in _os.environ:
                    _os.environ[key] = val
            break

_load_env()

import sys
from collections import defaultdict
from pathlib import Path

from faq_automation.core import read_questions
from faq_automation.evals.search_cases import ALL_CASES

from minsearch import Index


def build_index(documents):
    index = Index(
        text_fields=['question', 'answer'],
        keyword_fields=['course', 'section_id'],
    )
    index.fit(documents)
    return index


def recall_at_k(ranked_ids, relevant_ids, k):
    """Fraction of relevant docs found in top-k. With one relevant doc, this is hit@k."""
    if not relevant_ids:
        return 0.0
    found = sum(1 for rid in ranked_ids[:k] if rid in relevant_ids)
    return found / len(relevant_ids)


def mrr_at_k(ranked_ids, relevant_ids, k):
    """Reciprocal rank of the first relevant doc in top-k."""
    for i, rid in enumerate(ranked_ids[:k], 1):
        if rid in relevant_ids:
            return 1.0 / i
    return 0.0


def simulate_action(ranked_ids, relevant_ids, k):
    """Simulate the action decision from search results alone.

    If the relevant doc is in top-k -> FOUND (should be DUPLICATE/UPDATE).
    If not -> NEW. This is the search-level proxy for action accuracy
    without needing the LLM, so we can tune the index cheaply.
    """
    return 'FOUND' if any(rid in relevant_ids for rid in ranked_ids[:k]) else 'NEW'


def run_all(num_results=10, k_values=(1, 3, 5)):
    cases = ALL_CASES
    print(f"Search retrieval eval — {len(cases)} cases\n")

    # Load all documents per course
    docs_by_course = {}
    for course in sorted(set(c[0] for c in cases)):
        course_dir = Path('_questions') / course
        if not course_dir.exists():
            continue
        docs = read_questions(course_dir)
        docs_by_course[course] = docs
        print(f"  {course}: {len(docs)} documents")

    # Group cases by whether they have a relevant doc (positive) or not (negative)
    positive_cases = []  # doc_id != NONE — we know the relevant doc
    negative_cases = []  # doc_id == NONE — no relevant doc, testing false positives

    for course, query, relevant_id, issue_num, note in cases:
        if course not in docs_by_course:
            continue
        if relevant_id == 'NONE':
            negative_cases.append((course, query, relevant_id, issue_num, note))
        else:
            positive_cases.append((course, query, relevant_id, issue_num, note))

    # ===== POSITIVE EVAL =====
    print(f"\n{'='*60}")
    print(f"POSITIVE EVAL — {len(positive_cases)} positive cases")
    print("(target doc IN index — can search find it?)")
    print(f"{'='*60}")

    positive_results = []

    for course, query, relevant_id, issue_num, note in positive_cases:
        all_docs = docs_by_course[course]
        relevant_ids = {relevant_id}

        # Check that the doc actually exists in current corpus
        existing_ids = set(d['document_id'] for d in all_docs)
        if relevant_id not in existing_ids:
            continue

        index_full = build_index(all_docs)
        proposal = f"## {query}\n\n{query}"
        raw = index_full.search(proposal, num_results=num_results)
        ranked = [r.get('document_id', '') for r in raw]

        row = {
            'issue': issue_num,
            'course': course,
            'query': query[:70],
            'relevant_id': relevant_id,
            'ranked': ranked[:5],
            'note': note,
            'simulated_action': simulate_action(ranked, relevant_ids, 5),
        }
        for k in k_values:
            row[f'recall@{k}'] = recall_at_k(ranked, relevant_ids, k)
            row[f'mrr@{k}'] = mrr_at_k(ranked, relevant_ids, k)
        positive_results.append(row)

    n_positive = len(positive_results)
    if n_positive:
        print(f"\n{'issue':<7} {'course':<14} {'rec@5':<7} {'mrr@5':<7} {'rank':<5} {'query'}")
        print("-" * 95)
        for r in positive_results:
            rank = r['ranked'].index(r['relevant_id']) + 1 if r['relevant_id'] in r['ranked'] else -1
            note = f" [{r['note']}]" if r['note'] else ""
            print(f"  #{r['issue']:<5} {r['course'][:12]:<14} {r['recall@5']:<7.1f} {r['mrr@5']:<7.3f} {rank:<5} {r['query'][:45]}{note}")

        print(f"\nAggregate metrics ({n_positive} cases):")
        for k in k_values:
            avg_recall = sum(r[f'recall@{k}'] for r in positive_results) / n_positive
            avg_mrr = sum(r[f'mrr@{k}'] for r in positive_results) / n_positive
            print(f"  @{k}:  recall={avg_recall:.3f}  mrr={avg_mrr:.3f}")

        # Simulated action accuracy: all positive cases should be FOUND at k=5
        correct = sum(1 for r in positive_results if r['simulated_action'] == 'FOUND')
        print(f"\n  simulated action accuracy: {correct}/{n_positive} = {correct/n_positive:.3f}")
        print(f"  (FOUND = relevant doc in top-5; in production the LLM would decide DUPLICATE/UPDATE)")

        print(f"\nBy course:")
        by_course = defaultdict(list)
        for r in positive_results:
            by_course[r['course']].append(r)
        for course, rows in sorted(by_course.items()):
            nc = len(rows)
            rc = sum(r['recall@5'] for r in rows) / nc
            mc = sum(r['mrr@5'] for r in rows) / nc
            print(f"  {course}: recall@5={rc:.3f}  mrr@5={mc:.3f}  ({nc} cases)")

        failures = [r for r in positive_results if r['recall@5'] == 0.0]
        if failures:
            print(f"\nMisses ({len(failures)} — relevant doc not in top-5):")
            for r in failures:
                print(f"  #{r['issue']} expected={r['relevant_id']} got={r['ranked'][:3]}")

    # ===== NEGATIVE EVAL =====
    print(f"\n{'='*60}")
    print(f"NEGATIVE EVAL — {len(positive_cases)} + {len(negative_cases)} cases")
    print("(target doc REMOVED — testing false-positive risk for NEW proposals)")
    print(f"{'='*60}")

    # For positive cases: remove the target doc, search, see what comes back
    # For negative cases: search as-is (no removal needed)
    #
    # The question for each: would the top results mislead the LLM into calling
    # DUPLICATE? We measure: what fraction of top-1 results come from the same
    # section as the removed doc? (Same-section = more likely to look relevant.)

    negative_results = []

    for course, query, relevant_id, issue_num, note in positive_cases + negative_cases:
        all_docs = docs_by_course[course]
        relevant_ids = {relevant_id} if relevant_id != 'NONE' else set()

        filtered_docs = [d for d in all_docs if d['document_id'] not in relevant_ids]
        index_filtered = build_index(filtered_docs)
        proposal = f"## {query}\n\n{query}"
        raw_negative = index_filtered.search(proposal, num_results=num_results)
        negative_ranked = [(r.get('document_id', ''), r.get('section_id', '')) for r in raw_negative]

        # Find the section of the removed doc (for positive cases)
        removed_section = None
        if relevant_ids:
            for d in all_docs:
                if d['document_id'] in relevant_ids:
                    removed_section = d['section_id']
                    break

        # Check if top result is from the same section (potential false positive)
        top1_same_section = False
        if negative_ranked and removed_section:
            top1_same_section = negative_ranked[0][1] == removed_section

        negative_row = {
            'issue': issue_num,
            'course': course,
            'query': query[:70],
            'relevant_id': relevant_id,
            'removed_section': removed_section,
            'top5': negative_ranked[:5],
            'top1_same_section': top1_same_section,
            'note': note,
            'type': 'positive' if relevant_id != 'NONE' else 'negative',
        }
        negative_results.append(negative_row)

    # Summary
    pos_negative = [r for r in negative_results if r['type'] == 'positive']
    neg_negative = [r for r in negative_results if r['type'] == 'negative']

    if pos_negative:
        fp_rate = sum(1 for r in pos_negative if r['top1_same_section']) / len(pos_negative)
        print(f"\nPositive cases (doc removed, {len(pos_negative)} total):")
        print(f"  Top-1 from same section as removed doc: {fp_rate:.1%}")
        print(f"  (High rate = search returns same-topic matches that could trigger false DUPLICATE)")

    if neg_negative:
        print(f"\nNegative cases (no relevant doc, {len(neg_negative)} total):")
        for r in neg_negative:
            top = r['top5'][:3]
            top_str = ', '.join(f'{did}({sec[:8]})' for did, sec in top)
            print(f"  {r['query'][:50]}")
            print(f"    top3: {top_str}")

    # Show examples of potential false positives
    print(f"\nPotential false-positive examples (top-1 same section as removed doc):")
    fp_examples = [r for r in pos_negative if r['top1_same_section']][:10]
    for r in fp_examples:
        top1 = r['top5'][0] if r['top5'] else ('?', '?')
        print(f"  #{r['issue']} removed={r['relevant_id']}({r['removed_section']})")
        print(f"    query: {r['query'][:55]}")
        print(f"    got:   {top1[0]}({top1[1]})")
        print()

    total = len(positive_results)
    passed = sum(1 for r in positive_results if r['recall@5'] > 0)
    return passed == total


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run search retrieval eval')
    parser.add_argument('--num-results', type=int, default=10)
    args = parser.parse_args()

    success = run_all(num_results=args.num_results)
    sys.exit(0 if success else 1)
