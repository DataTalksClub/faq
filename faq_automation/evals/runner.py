"""
Eval runner for the FAQ merge agent.

Runs each eval case through the real FAQAgent (with live LLM call) against the
current _questions/ state. Since entries may already exist in the FAQ, the runner
dynamically adjusts the expected action: if the entry already exists, the correct
answer is DUPLICATE. If it doesn't, it uses the case's declared expected_action.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.runner
    uv run --project faq_automation python -m faq_automation.evals.runner --issue 303
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

import os
import sys
from pathlib import Path
from collections import defaultdict

from faq_automation.rag_agent import FAQAgent, DEFAULT_MODEL
from faq_automation.core import read_questions

from faq_automation.evals.cases import CASES, EvalCase


def get_existing_doc_ids(course_dir):
    """Return set of all doc_ids currently in the course."""
    docs = read_questions(course_dir)
    return set(d['document_id'] for d in docs)


def get_section_sort_orders(course_dir):
    """Return {section_id: set(sort_orders)}."""
    docs = read_questions(course_dir)
    orders = defaultdict(set)
    for d in docs:
        orders[d['section_id']].add(d['sort_order'])
    return dict(orders)


def run_case(case, agent, existing_ids, section_sort_orders):
    """Run a single eval case and return results."""
    # Dynamically adjust: if the case's doc_id already exists, expect DUPLICATE
    # We infer the doc_id from the issue — but we don't store it per case.
    # Instead: the search results will tell us. If the agent returns DUPLICATE
    # pointing to a doc whose question matches the case, that's correct.
    #
    # For now, just run it and see what the agent decides.
    print(f"\n{'='*60}")
    print(f"Issue #{case.issue_number}: {case.question[:80]}")
    print(f"Expected: {case.expected_action}")
    print(f"{'='*60}")

    decision = agent.process_proposal(case.question, case.answer)

    print(f"Got: action={decision.action}, section={decision.section_id}, order={decision.order}")

    results = []

    for check in case.checks:
        if hasattr(check, '__name__') and 'sort_order' in check.__name__:
            existing = section_sort_orders.get(case.expected_section or decision.section_id, set())
            from faq_automation.evals.cases import no_sort_order_collision
            check = no_sort_order_collision(existing)

        try:
            passed = check(decision)
        except Exception as e:
            passed = False
            print(f"  CHECK ERROR: {e}")

        name = getattr(check, '__name__', str(check))
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        results.append({'check': name, 'passed': passed})

    return {
        'issue': case.issue_number,
        'question': case.question[:80],
        'description': case.description,
        'expected_action': case.expected_action,
        'got_action': decision.action,
        'got_section': decision.section_id,
        'got_order': decision.order,
        'rationale': decision.rationale,
        'results': results,
        'all_passed': all(r['passed'] for r in results),
        'tags': case.tags,
    }


def run_all(model=DEFAULT_MODEL, issue_number=None):
    cases = CASES
    if issue_number is not None:
        cases = [case for case in CASES if case.issue_number == issue_number]
        if not cases:
            print(f"Error: no eval case found for issue #{issue_number}", file=sys.stderr)
            return False

    print(f"Running FAQ merge agent evals")
    print(f"  model: {model}")
    if issue_number is not None:
        print(f"  issue: #{issue_number}")
    print(f"Total cases: {len(cases)}")

    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    # Build agents per (course, removed_doc) combo
    # When a case expects NEW and has a relevant_doc_id, we remove that doc
    # so the agent can't trivially find it as a duplicate — same as the NOISE eval.
    agents = {}
    section_orders_cache = {}
    existing_ids_cache = {}

    def get_agent(course, remove_doc_id):
        """Get or create an agent for a course, optionally with a doc removed."""
        key = (course, remove_doc_id)
        if key not in agents:
            course_dir = Path('_questions') / course
            if not course_dir.exists():
                return None, None, None
            if remove_doc_id:
                # Create a temp copy with the doc removed
                import tempfile, shutil
                tmpdir = tempfile.mkdtemp()
                tmp_course = Path(tmpdir) / course
                shutil.copytree(course_dir, tmp_course)
                # Remove the file matching the doc_id
                for f in tmp_course.glob('*/*.md'):
                    parts = f.name.split('_', maxsplit=2)
                    if len(parts) >= 2 and parts[1] == remove_doc_id:
                        f.unlink()
                        print(f"  [hidden] removed {f.name} from {course} for eval")
                        break
                course_dir = tmp_course
            agents[key] = FAQAgent(course_dir, api_key, model)
            section_orders_cache[key] = get_section_sort_orders(course_dir)
            existing_ids_cache[key] = get_existing_doc_ids(course_dir)
        return agents[key], section_orders_cache[key], existing_ids_cache[key]

    all_results = []

    for case in cases:
        # Hide the relevant doc when we expect NEW (so the agent can't find it)
        remove_doc = case.relevant_doc_id if case.expected_action == 'NEW' and case.relevant_doc_id else None
        agent, section_orders, existing_ids = get_agent(case.course, remove_doc)
        if agent is None:
            continue
        result = run_case(case, agent, existing_ids, section_orders)
        all_results.append(result)

    # Summary
    print(f"\n\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    total = len(all_results)
    passed = sum(1 for r in all_results if r['all_passed'])
    failed = total - passed

    for r in all_results:
        status = "PASS" if r['all_passed'] else "FAIL"
        failed_checks = [x['check'] for x in r['results'] if not x['passed']]
        detail = f" (failed: {', '.join(failed_checks)})" if failed_checks else ""
        print(f"  [{status}] #{r['issue']}: {r['question'][:55]}{detail}")
        if not r['all_passed']:
            print(f"         got: action={r['got_action']}, section={r['got_section']}")

    print(f"\n{passed}/{total} cases passed ({failed} failed)")

    # Pattern analysis
    print(f"\n{'='*60}")
    print("PATTERN ANALYSIS")
    print(f"{'='*60}")

    pattern_failures = defaultdict(int)
    for r in all_results:
        for check in r['results']:
            if not check['passed']:
                pattern_failures[check['check']] += 1

    if pattern_failures:
        for pattern, count in sorted(pattern_failures.items(), key=lambda x: -x[1]):
            print(f"  {count}x  {pattern}")
    else:
        print("  All checks passed!")

    # Tag analysis
    print(f"\n{'='*60}")
    print("FAILURE BY TAG")
    print(f"{'='*60}")
    tag_failures = defaultdict(int)
    tag_totals = defaultdict(int)
    for r in all_results:
        for tag in r['tags']:
            tag_totals[tag] += 1
            if not r['all_passed']:
                tag_failures[tag] += 1
    if tag_failures:
        for tag in sorted(tag_failures.keys()):
            print(f"  {tag}: {tag_failures[tag]}/{tag_totals[tag]} failed")

    return failed == 0


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run FAQ merge agent evals')
    parser.add_argument('--model', default=DEFAULT_MODEL)
    parser.add_argument('--issue', type=int, help='Run only eval cases from this GitHub issue')
    args = parser.parse_args()

    success = run_all(model=args.model, issue_number=args.issue)
    sys.exit(0 if success else 1)
