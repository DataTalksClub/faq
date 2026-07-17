"""
Search/retrieval eval for the FAQ merge agent.

Tests the retrieval layer (minsearch index) in isolation — no LLM calls, runs
in seconds. Each case is a real issue question paired with the doc_id of the
FAQ entry it became. We search the current index (which contains that entry)
and measure whether the search surfaces the right doc.

  Metrics: recall@k (= hit_rate@k), MRR@k.

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
    cases = [c for c in ALL_CASES if c.answer != 'NONE']
    print(f"Search retrieval eval — {len(cases)} cases\n")

    # Load all documents per course
    docs_by_course = {}
    for course in sorted(set(c.course for c in cases)):
        course_dir = Path('_questions') / course
        if not course_dir.exists():
            continue
        docs = read_questions(course_dir)
        docs_by_course[course] = docs
        print(f"  {course}: {len(docs)} documents")

    # Build index per course
    indices = {}
    for course, docs in docs_by_course.items():
        indices[course] = build_index(docs)

    results = []

    for case in cases:
        if case.course not in indices:
            continue

        all_docs = docs_by_course[case.course]
        existing_ids = set(d['document_id'] for d in all_docs)
        if case.doc_id not in existing_ids:
            continue

        relevant_ids = {case.doc_id}
        index = indices[case.course]
        proposal = f"## {case.question}\n\n{case.answer}" if case.answer else f"## {case.question}\n\n{case.question}"
        raw = index.search(proposal, num_results=num_results)
        ranked = [r.get('document_id', '') for r in raw]

        row = {
            'case': case.case_id,
            'course': case.course,
            'query': case.question[:70],
            'relevant_id': case.doc_id,
            'ranked': ranked[:5],
            'note': case.note,
        }
        for k in k_values:
            row[f'recall@{k}'] = recall_at_k(ranked, relevant_ids, k)
            row[f'mrr@{k}'] = mrr_at_k(ranked, relevant_ids, k)
        results.append(row)

    n = len(results)
    if not n:
        print("No cases with valid doc_ids found in current corpus.")
        return

    # Per-query detail
    print(f"\n{'case':<7} {'course':<14} {'rec@5':<7} {'mrr@5':<7} {'rank':<5} {'query'}")
    print("-" * 95)
    for r in results:
        rank = r['ranked'].index(r['relevant_id']) + 1 if r['relevant_id'] in r['ranked'] else -1
        note_str = f" [{r['note']}]" if r['note'] else ""
        print(f"  #{r['case']:<5} {r['course'][:12]:<14} {r['recall@5']:<7.1f} {r['mrr@5']:<7.3f} {rank:<5} {r['query'][:45]}{note_str}")

    # Aggregate metrics
    print(f"\n{'='*60}")
    print(f"Aggregate metrics ({n} cases)")
    print(f"{'='*60}")
    for k in k_values:
        avg_recall = sum(r[f'recall@{k}'] for r in results) / n
        avg_mrr = sum(r[f'mrr@{k}'] for r in results) / n
        print(f"  @{k}:  recall={avg_recall:.3f}  mrr={avg_mrr:.3f}")

    # By course
    print(f"\nBy course:")
    by_course = defaultdict(list)
    for r in results:
        by_course[r['course']].append(r)
    for course, rows in sorted(by_course.items()):
        nc = len(rows)
        rc = sum(r['recall@5'] for r in rows) / nc
        mc = sum(r['mrr@5'] for r in rows) / nc
        print(f"  {course}: recall@5={rc:.3f}  mrr@5={mc:.3f}  ({nc} cases)")

    # Failures
    failures = [r for r in results if r['recall@5'] == 0.0]
    if failures:
        print(f"\nMisses ({len(failures)} — relevant doc not in top-5):")
        for r in failures:
            print(f"  #{r['case']} expected={r['relevant_id']} got={r['ranked'][:3]}")

    total = len(results)
    passed = sum(1 for r in results if r['recall@5'] > 0)
    return passed == total


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run search retrieval eval')
    parser.add_argument('--num-results', type=int, default=10)
    args = parser.parse_args()

    success = run_all(num_results=args.num_results)
    sys.exit(0 if success else 1)
