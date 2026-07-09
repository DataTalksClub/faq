"""
Eval runner for the FAQ merge agent.

Runs each eval case through the real FAQAgent (with live LLM call) against a
snapshot of _questions/ at the right base commit for each case — so the agent
sees the same state it would have seen when the proposal was originally processed.

Each case can specify its own base_commit. Cases without one fall back to the
--base-commit argument.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.runner
"""

import os as _os
from pathlib import Path as _Path

def _load_env():
    """Load .env from repo root into os.environ if not already set."""
    for candidate in [_Path(__file__).resolve().parents[3], _Path.cwd()]:
        env_file = candidate / '.env'
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, _, val = line.partition('=')
                key, val = key.strip(), val.strip()
                if key not in _os.environ:
                    _os.environ[key] = val
            break

_load_env()

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from collections import defaultdict

from faq_automation.rag_agent import FAQAgent
from faq_automation.core import read_questions

from faq_automation.evals.cases import CASES, EvalCase


# Cache of course dirs per base commit to avoid re-archiving
_snapshot_cache: dict[tuple[str, str], Path] = {}


def snapshot_course_at_commit(commit: str, course: str, dest_root: Path) -> Path:
    """Extract _questions/<course>/ from a git commit into dest_root, return the course dir."""
    cache_key = (commit, course)
    if cache_key in _snapshot_cache:
        return _snapshot_cache[cache_key]

    result = subprocess.run(
        ['git', 'archive', commit, f'_questions/{course}'],
        capture_output=True, check=True
    )
    dest = dest_root / course
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            ['tar', '-x', '-C', tmpdir],
            input=result.stdout, check=True
        )
        src = Path(tmpdir) / '_questions' / course
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)

    _snapshot_cache[cache_key] = dest
    return dest


def get_section_sort_orders(course_dir: Path) -> dict:
    """Return {section_id: set(sort_orders)} for a course."""
    docs = read_questions(course_dir)
    section_orders = defaultdict(set)
    for doc in docs:
        section_orders[doc['section_id']].add(doc['sort_order'])
    return dict(section_orders)


def run_case(case: EvalCase, agent: FAQAgent, section_sort_orders: dict) -> dict:
    """Run a single eval case and return results."""
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
            check = _make_collision_check(existing)

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


def _make_collision_check(existing_orders):
    from faq_automation.evals.cases import no_sort_order_collision
    return no_sort_order_collision(existing_orders)


def run_all(model: str = "gpt-5.4-nano", default_base_commit: str = "HEAD"):
    """Run all eval cases against per-case base commits."""
    print(f"Running FAQ merge agent evals")
    print(f"  model: {model}")
    print(f"  default base commit: {default_base_commit}")
    print(f"Total cases: {len(CASES)}")

    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    # Group cases by (course, base_commit) to batch agent creation
    all_results = []

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_root = Path(tmpdir) / '_questions'
        tmp_root.mkdir()

        # Process cases grouped by course+commit for agent reuse
        agents: dict[tuple[str, str], FAQAgent] = {}
        sort_orders: dict[tuple[str, str], dict] = {}

        for case in CASES:
            commit = case.base_commit or default_base_commit
            key = (case.course, commit)

            if key not in agents:
                course_dir = snapshot_course_at_commit(commit, case.course, tmp_root)
                agents[key] = FAQAgent(course_dir, api_key, model)
                sort_orders[key] = get_section_sort_orders(course_dir)

            print(f"\n{'#'*60}")
            print(f"# Course: {case.course} @ {commit[:12]}")
            print(f"{'#'*60}")

            result = run_case(case, agents[key], sort_orders[key])
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
            total_t = tag_totals[tag]
            failed_t = tag_failures[tag]
            print(f"  {tag}: {failed_t}/{total_t} failed")

    return failed == 0


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run FAQ merge agent evals')
    parser.add_argument('--model', default='gpt-5.4-nano', help='OpenAI model to use')
    parser.add_argument('--base-commit', default='HEAD',
                        help='Default base commit for cases without their own')
    args = parser.parse_args()

    success = run_all(model=args.model, default_base_commit=args.base_commit)
    sys.exit(0 if success else 1)
