"""
Search tuning harness for the FAQ merge agent.

Sweeps boost configurations and text-field selections for the minsearch index.
Reports recall@5 and MRR@5 per config. No LLM calls, runs in seconds.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.tune_search
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
from pathlib import Path
from collections import defaultdict

from faq_automation.core import read_questions
from faq_automation.evals.search_cases import ALL_CASES

from minsearch import Index

K = 5


def build_index(documents, text_fields):
    index = Index(
        text_fields=text_fields,
        keyword_fields=['course', 'section_id'],
    )
    index.fit(documents)
    return index


def evaluate_config(docs_by_course, text_fields, boosts=None, num_results=10):
    """Evaluate a config against all cases. Returns metrics dict."""
    indices = {}
    for course, docs in docs_by_course.items():
        indices[course] = build_index(docs, text_fields)

    recalls = []
    mrrs = []

    for case in ALL_CASES:
        if case.course not in indices:
            continue
        if case.doc_id == 'NONE':
            continue

        all_docs = docs_by_course[case.course]
        existing_ids = set(d['document_id'] for d in all_docs)
        if case.doc_id not in existing_ids:
            continue

        relevant_ids = {case.doc_id}
        index = indices[case.course]
        proposal = f"## {case.question}\n\n{case.answer}" if case.answer else f"## {case.question}\n\n{case.question}"
        raw = index.search(proposal, boost_dict=boosts, num_results=num_results)
        ranked = [r.get('document_id', '') for r in raw]

        found = case.doc_id in ranked[:K]
        recalls.append(1.0 if found else 0.0)

        mrr = 0.0
        for i, rid in enumerate(ranked[:K], 1):
            if rid in relevant_ids:
                mrr = 1.0 / i
                break
        mrrs.append(mrr)

    n = len(recalls)
    if n == 0:
        return None

    return {
        'n': n,
        'recall@5': sum(recalls) / n,
        'mrr@5': sum(mrrs) / n,
    }


def run_tuning():
    print("Search tuning — sweeping boost and text-field configurations\n")

    docs_by_course = {}
    for course in sorted(set(c.course for c in ALL_CASES)):
        course_dir = Path('_questions') / course
        if not course_dir.exists():
            continue
        docs = read_questions(course_dir)
        docs_by_course[course] = docs
        print(f"  {course}: {len(docs)} docs")

    field_configs = [
        ('q+a+section', ['question', 'answer', 'section']),
        ('q+a (no section)', ['question', 'answer']),
    ]

    boost_configs = {
        'no boosts': None,
        'question x3': {'question': 3.0, 'answer': 1.0, 'section': 1.0},
        'question x5': {'question': 5.0, 'answer': 1.0, 'section': 1.0},
        'question x3, answer x0.5': {'question': 3.0, 'answer': 0.5, 'section': 1.0},
    }

    results = []
    for field_name, fields in field_configs:
        for boost_name, boosts in boost_configs.items():
            # For q+a config, drop section from boosts
            if 'section' not in fields and boosts:
                boosts = {k: v for k, v in boosts.items() if k != 'section'}
            full_name = f"{boost_name} | {field_name}"
            metrics = evaluate_config(docs_by_course, fields, boosts=boosts)
            if metrics:
                results.append((full_name, boosts, metrics))

    print(f"\n{'config':<45} {'recall@5':<10} {'mrr@5':<10}")
    print("-" * 65)
    for name, boosts, m in results:
        print(f"{name:<45} {m['recall@5']:<10.3f} {m['mrr@5']:<10.3f}")

    best_rec = max(results, key=lambda x: x[2]['recall@5'])
    best_mrr = max(results, key=lambda x: x[2]['mrr@5'])
    print(f"\nBest recall@5: {best_rec[0]} = {best_rec[2]['recall@5']:.3f}")
    print(f"Best MRR@5:    {best_mrr[0]} = {best_mrr[2]['mrr@5']:.3f}")


if __name__ == '__main__':
    run_tuning()
