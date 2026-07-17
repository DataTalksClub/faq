"""
Eval runner for the FAQ merge agent.

Runs each eval case through the real FAQAgent against the current _questions/
state. Since entries may already exist in the FAQ, the runner dynamically adjusts
the expected action: if the entry already exists, the correct answer is DUPLICATE.
If it doesn't, it uses the case's declared expected_action.

Cases run on the flex tier by default: the same discounted rate as the Batch API,
but answers come back now instead of whenever the batch queue drains. --batch
submits the suite as one Batch API job for the same price when nobody is waiting.
Either way, retrieval and prompt assembly happen locally, so only the model calls
leave the machine.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.runner
    uv run --project faq_automation python -m faq_automation.evals.runner --issue 303
    uv run --project faq_automation python -m faq_automation.evals.runner --batch
    uv run --project faq_automation python -m faq_automation.evals.runner --batch-id batch_abc123
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
import tempfile
from pathlib import Path
from collections import defaultdict

from openai import OpenAI

from faq_automation.rag_agent import FAQAgent, DEFAULT_MODEL
from faq_automation.core import read_questions

from faq_automation.evals import batch, flex
from faq_automation.evals.cases import CASES, EvalCase, not_wrong_course


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


def evaluate(case, decision, section_sort_orders):
    """Score one decision against its case's checks and return the result row."""
    print(f"\n{'='*60}")
    print(f"Issue #{case.issue_number}: {case.question[:80]}")
    print(f"Expected: {case.expected_action}")
    print(f"{'='*60}")

    if decision is None:
        print("  MISSING: no decision returned for this case")
        return {
            'issue': case.issue_number,
            'question': case.question[:80],
            'description': case.description,
            'expected_action': case.expected_action,
            'got_action': 'MISSING',
            'got_section': '',
            'got_order': None,
            'rationale': 'no decision returned',
            'results': [{'check': 'decision returned', 'passed': False}],
            'all_passed': False,
            'tags': case.tags,
        }

    print(f"Got: action={decision.action}, section={decision.section_id}, order={decision.order}")

    results = []

    checks = list(case.checks)

    # Every case that isn't about the wrong course is a false-positive guard for
    # WRONG_COURSE: rejecting a valid proposal is worse than misplacing it.
    if case.expected_action != 'WRONG_COURSE':
        checks.insert(0, not_wrong_course)

    for check in checks:
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


def collect_decisions_batch(prepared, model, batch_id=None, output_dir=None):
    """
    Send every case as one Batch API job and return decisions in `prepared` order.

    A case whose request failed gets None, so evaluate() can fail it explicitly
    rather than let a partial run score as a pass. Pass batch_id to re-read an
    already-submitted job instead of paying for a new one.
    """
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    if output_dir is None:
        output_dir = Path(tempfile.mkdtemp())

    custom_ids = []
    for index, (case, _, _) in enumerate(prepared):
        custom_ids.append(f"case-{index}-issue-{case.issue_number}")

    if batch_id is None:
        requests = []
        for custom_id, (case, agent, _) in zip(custom_ids, prepared):
            messages = agent.build_messages(case.question, case.answer)
            requests.append(batch.build_request(custom_id, messages, model))

        input_path = output_dir / 'eval_batch_input.jsonl'
        batch_id = batch.submit(client, requests, input_path)
        print(f"\nSubmitted batch {batch_id} ({len(requests)} requests)")
        print(f"  input file: {input_path}")
        print(f"  resume with: --batch-id {batch_id}")
    else:
        print(f"\nReusing batch {batch_id}")

    print("\nWaiting for the batch to finish...")
    job = batch.poll(client, batch_id)

    if job.status != 'completed':
        print(f"Error: batch {batch_id} ended as {job.status}", file=sys.stderr)

    by_custom_id = batch.fetch(client, job)

    decisions = []
    for custom_id in custom_ids:
        decisions.append(by_custom_id.get(custom_id))
    return decisions


def collect_decisions(prepared, model, use_batch=False, batch_id=None):
    """Run every prepared case and return decisions in `prepared` order."""
    if use_batch or batch_id:
        return collect_decisions_batch(prepared, model, batch_id=batch_id)

    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    print(f"\nRunning {len(prepared)} cases on the flex tier ({flex.MAX_WORKERS} at a time)...")
    return flex.collect(client, prepared, model)


def run_all(model=DEFAULT_MODEL, issue_number=None, use_batch=False, batch_id=None):
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
            # questions_dir stays on the repo so the course catalog is the real
            # one even when course_dir is a temp copy with a doc removed.
            agents[key] = FAQAgent(course_dir, api_key, model, questions_dir=Path('_questions'))
            section_orders_cache[key] = get_section_sort_orders(course_dir)
            existing_ids_cache[key] = get_existing_doc_ids(course_dir)
        return agents[key], section_orders_cache[key], existing_ids_cache[key]

    prepared = []

    for case in cases:
        # Hide the relevant doc when we expect NEW (so the agent can't find it)
        remove_doc = case.relevant_doc_id if case.expected_action == 'NEW' and case.relevant_doc_id else None
        agent, section_orders, existing_ids = get_agent(case.course, remove_doc)
        if agent is None:
            continue
        prepared.append((case, agent, section_orders))

    decisions = collect_decisions(prepared, model, use_batch=use_batch, batch_id=batch_id)

    all_results = []

    for (case, _, section_orders), decision in zip(prepared, decisions):
        all_results.append(evaluate(case, decision, section_orders))

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
    parser.add_argument('--batch', action='store_true',
                        help='Submit one Batch API job instead of running on the flex tier. '
                             'Same price, but results can take hours to come back.')
    parser.add_argument('--batch-id',
                        help='Score an already-submitted batch job instead of submitting a new one')
    args = parser.parse_args()

    success = run_all(
        model=args.model,
        issue_number=args.issue,
        use_batch=args.batch,
        batch_id=args.batch_id,
    )
    sys.exit(0 if success else 1)
