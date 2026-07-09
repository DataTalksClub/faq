"""
Search/retrieval eval for the FAQ merge agent.

For each case, the ground-truth relevant doc is removed from the index before
searching, so the corpus reflects the state the agent was in when the proposal
was first processed. This lets us measure:

  - For DUPLICATE/UPDATE cases (relevant doc known): can the search find the
    right doc if we put it back in? -> recall, precision, MRR
  - For NEW cases (no relevant doc): does the search return weak enough matches
    so the agent won't wrongly call DUPLICATE? -> score distribution / separation

Actually, the opposite is needed: the agent searches WITH the doc in the index
(for DUPLICATE detection). For NEW cases, the doc should NOT be in the index.

Since all docs are currently in the index, we handle it per-case:
  - Cases where the doc exists: remove it, then search (tests: can the agent
    still find it if needed? put it back and search — but that defeats the purpose).

Simpler framing — two complementary measurements:

  1. FIND eval: keep the doc IN the index. Can search find it? (recall@k, MRR)
     This tests whether the agent would correctly identify a DUPLICATE.

  2. NOISE eval: remove the doc. What does search return instead?
     Are the top results noisy (good for NEW) or high-confidence false matches
     (bad — would trigger a false DUPLICATE)?

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
from copy import deepcopy
from pathlib import Path

from faq_automation.core import read_questions
from faq_automation.evals.search_cases import ALL_CASES

from minsearch import Index


def build_index(documents):
    index = Index(
        text_fields=['section', 'question', 'answer'],
        keyword_fields=['course', 'section_id'],
    )
    index.fit(documents)
    return index


def hit_at_k(ranked_ids, relevant_ids, k):
    return 1.0 if any(rid in relevant_ids for rid in ranked_ids[:k]) else 0.0


def mrr_at_k(ranked_ids, relevant_ids, k):
    for i, rid in enumerate(ranked_ids[:k], 1):
        if rid in relevant_ids:
            return 1.0 / i
    return 0.0


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

    find_results = []   # doc IN index: can search find it?
    noise_results = []  # doc REMOVED: what comes back instead?

    for course, query, relevant_id, issue_num, note in cases:
        if course not in docs_by_course:
            continue

        all_docs = docs_by_course[course]
        relevant_ids = {relevant_id} if relevant_id != 'NONE' else set()

        # --- FIND eval: doc is in the index ---
        index_full = build_index(all_docs)
        proposal = f"## {query}\n\n{query}"
        raw = index_full.search(proposal, num_results=num_results)
        ranked = [r.get('document_id', '') for r in raw]

        if relevant_ids:
            find_row = {
                'issue': issue_num,
                'course': course,
                'query': query[:70],
                'relevant_id': relevant_id,
                'ranked': ranked[:5],
                'note': note,
            }
            for k in k_values:
                find_row[f'hit@{k}'] = hit_at_k(ranked, relevant_ids, k)
                find_row[f'mrr@{k}'] = mrr_at_k(ranked, relevant_ids, k)
            find_results.append(find_row)

        # --- NOISE eval: doc removed from index ---
        filtered_docs = [d for d in all_docs if d['document_id'] not in relevant_ids]
        index_filtered = build_index(filtered_docs)
        raw_noise = index_filtered.search(proposal, num_results=num_results)
        noise_ranked = [(r.get('document_id', ''), r.get('section_id', '')) for r in raw_noise]

        noise_row = {
            'issue': issue_num,
            'course': course,
            'query': query[:70],
            'relevant_id': relevant_id,
            'top5': noise_ranked[:5],
            'note': note,
            'is_new': relevant_id != 'NONE' and relevant_id not in set(d['document_id'] for d in all_docs),
        }
        noise_results.append(noise_row)

    # ===== FIND eval results =====
    print(f"\n{'='*60}")
    print("FIND EVAL (doc in index — can search find it?)")
    print(f"{'='*60}")

    n = len(find_results)
    if n == 0:
        print("  No cases with known relevant doc_id")
    else:
        print(f"\n{'issue':<7} {'hit@5':<6} {'rank':<5} {'query':<60}")
        print("-" * 80)
        for r in find_results:
            rank = -1
            if r['relevant_id'] in r['ranked']:
                rank = r['ranked'].index(r['relevant_id']) + 1
            hit = 'Y' if r['hit@5'] else 'N'
            note = f" [{r['note']}]" if r['note'] else ""
            print(f"  #{r['issue']:<5} {hit:<6} {rank:<5} {r['query'][:55]}{note}")

        print(f"\nMetrics ({n} cases):")
        for k in k_values:
            avg_hit = sum(r[f'hit@{k}'] for r in find_results) / n
            avg_mrr = sum(r[f'mrr@{k}'] for r in find_results) / n
            print(f"  hit@{k}: {avg_hit:.3f}   mrr@{k}: {avg_mrr:.3f}")

        print(f"\nBy course:")
        by_course = defaultdict(list)
        for r in find_results:
            by_course[r['course']].append(r)
        for course, rows in sorted(by_course.items()):
            nc = len(rows)
            h5 = sum(r['hit@5'] for r in rows) / nc
            m5 = sum(r['mrr@5'] for r in rows) / nc
            print(f"  {course}: hit@5={h5:.3f}  mrr@5={m5:.3f}  ({nc} cases)")

        failures = [r for r in find_results if not r['hit@5']]
        if failures:
            print(f"\nFailures ({len(failures)} missed at k=5):")
            for r in failures:
                print(f"  #{r['issue']} expected={r['relevant_id']} got={r['ranked']}")
                if r['note']:
                    print(f"    note: {r['note']}")

    # ===== NOISE eval results =====
    print(f"\n{'='*60}")
    print("NOISE EVAL (doc removed — what comes back instead?)")
    print(f"{'='*60}")

    # For NEW-type queries (relevant doc was NEW, so shouldn't have matched anything):
    # check whether the top results are from a completely different topic
    new_type = [r for r in noise_results if r['relevant_id'] != 'NONE']
    print(f"\n{len(new_type)} cases where the entry was created as NEW")
    print("(top results should ideally be unrelated — if they're strong matches,")
    print("the agent would wrongly call DUPLICATE)\n")

    for r in new_type[:15]:
        top = r['top5'][:3]
        top_str = ', '.join(f'{did}({sec[:8]})' for did, sec in top)
        print(f"  #{r['issue']:<5} {r['query'][:50]}")
        print(f"         top3: {top_str}")

    print()
    total = len(find_results)
    passed = sum(1 for r in find_results if r['hit@5'])
    return passed == total


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run search retrieval eval')
    parser.add_argument('--num-results', type=int, default=10)
    args = parser.parse_args()

    success = run_all(num_results=args.num_results)
    sys.exit(0 if success else 1)
