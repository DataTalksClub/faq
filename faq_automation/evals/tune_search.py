"""
Search tuning harness for the FAQ merge agent.

Sweeps boost configurations for the minsearch index and reports how each
configuration affects recall@5, section_acc@5, top1_section_hit, and simulated
action accuracy. Runs in seconds per config — no LLM calls.

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
TEXT_FIELDS = ['section', 'question', 'answer']
KEYWORD_FIELDS = ['course', 'section_id']


def build_index(documents, boosts=None):
    index = Index(text_fields=TEXT_FIELDS, keyword_fields=KEYWORD_FIELDS)
    index.fit(documents)
    return index


def evaluate_config(docs_by_course, boosts=None, num_results=10):
    """Evaluate a boost configuration against all cases. Returns metrics dict."""
    indices = {}
    for course, docs in docs_by_course.items():
        indices[course] = build_index(docs)

    recalls = []
    section_accs = []
    top1_hits = []
    actions_correct = []

    for course, query, relevant_id, issue_num, note in ALL_CASES:
        if course not in indices:
            continue
        if relevant_id == 'NONE':
            continue

        all_docs = docs_by_course[course]
        existing_ids = set(d['document_id'] for d in all_docs)
        if relevant_id not in existing_ids:
            continue

        relevant_ids = {relevant_id}
        relevant_section = None
        for d in all_docs:
            if d['document_id'] in relevant_ids:
                relevant_section = d['section_id']
                break

        index = indices[course]
        proposal = f"## {query}\n\n{query}"
        raw = index.search(proposal, boost_dict=boosts, num_results=num_results)
        ranked_ids = [r.get('document_id', '') for r in raw]
        ranked_docs = [(r.get('document_id', ''), r.get('section_id', '')) for r in raw]

        # recall@k
        found = relevant_id in ranked_ids[:K]
        recalls.append(1.0 if found else 0.0)

        # section_acc@k
        if relevant_section and ranked_docs:
            same = sum(1 for _, sec in ranked_docs[:K] if sec == relevant_section)
            section_accs.append(same / min(K, len(ranked_docs)))
        else:
            section_accs.append(0.0)

        # top1_section_hit
        if relevant_section and ranked_docs:
            top1_hits.append(1.0 if ranked_docs[0][1] == relevant_section else 0.0)
        else:
            top1_hits.append(0.0)

        # simulated action accuracy
        actions_correct.append(1.0 if found else 0.0)

    n = len(recalls)
    if n == 0:
        return None

    return {
        'n': n,
        'recall@5': sum(recalls) / n,
        'section_acc@5': sum(section_accs) / n,
        'top1_section_hit': sum(top1_hits) / n,
        'action_acc': sum(actions_correct) / n,
    }


def run_tuning():
    print("Search tuning — sweeping boost configurations\n")

    # Load documents per course
    docs_by_course = {}
    for course in sorted(set(c[0] for c in ALL_CASES)):
        course_dir = Path('_questions') / course
        if not course_dir.exists():
            continue
        docs = read_questions(course_dir)
        docs_by_course[course] = docs
        print(f"  {course}: {len(docs)} docs")

    # Define configs to sweep
    configs = {
        'baseline (no boosts)': None,
        'question x3': {'question': 3.0, 'answer': 1.0, 'section': 1.0},
        'question x5': {'question': 5.0, 'answer': 1.0, 'section': 1.0},
        'question x3, section x0.5': {'question': 3.0, 'answer': 1.0, 'section': 0.5},
        'question x5, section x0': {'question': 5.0, 'answer': 1.0, 'section': 0.0},
        'question x3, answer x0.5': {'question': 3.0, 'answer': 0.5, 'section': 1.0},
        'question x5, answer x0.5': {'question': 5.0, 'answer': 0.5, 'section': 1.0},
    }

    # Also sweep text field configurations
    field_configs = [
        ('fields: q+a+section', ['section', 'question', 'answer']),
        ('fields: q+a (no section text)', ['question', 'answer']),
        ('fields: q only', ['question']),
    ]

    # Run each config across all field configurations
    global TEXT_FIELDS
    results = []
    for field_name, fields in field_configs:
        TEXT_FIELDS = fields
        for name, boosts in configs.items():
            full_name = f"{name} | {field_name}"
            metrics = evaluate_config(docs_by_course, boosts=boosts)
            if metrics:
                results.append((full_name, boosts, metrics))

    # Print results table
    print(f"\n{'config':<35} {'recall@5':<10} {'sec_acc@5':<10} {'top1_sec':<10} {'action':<10}")
    print("-" * 75)
    for name, boosts, m in results:
        print(f"{name:<35} {m['recall@5']:<10.3f} {m['section_acc@5']:<10.3f} {m['top1_section_hit']:<10.3f} {m['action_acc']:<10.3f}")

    # Find best configs
    print(f"\nBest by section_acc@5:")
    best_sec = max(results, key=lambda x: x[2]['section_acc@5'])
    print(f"  {best_sec[0]}: {best_sec[2]['section_acc@5']:.3f}")

    print(f"\nBest by recall@5:")
    best_rec = max(results, key=lambda x: x[2]['recall@5'])
    print(f"  {best_rec[0]}: {best_rec[2]['recall@5']:.3f}")

    print(f"\nBest by top1_section_hit:")
    best_top1 = max(results, key=lambda x: x[2]['top1_section_hit'])
    print(f"  {best_top1[0]}: {best_top1[2]['top1_section_hit']:.3f}")

    # Combined score (weighted average prioritizing section_acc)
    print(f"\nBest by combined score (0.5*sec_acc + 0.3*recall + 0.2*top1):")
    best_combined = max(results, key=lambda x: 0.5 * x[2]['section_acc@5'] + 0.3 * x[2]['recall@5'] + 0.2 * x[2]['top1_section_hit'])
    m = best_combined[2]
    print(f"  {best_combined[0]}: sec_acc={m['section_acc@5']:.3f} recall={m['recall@5']:.3f} top1={m['top1_section_hit']:.3f}")
    print(f"  boosts: {best_combined[1]}")


if __name__ == '__main__':
    run_tuning()
