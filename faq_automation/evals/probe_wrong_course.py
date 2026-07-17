"""
Measure WRONG_COURSE recall and false-positive rate across repeats.

The main runner scores each case once, which hides how much the decision moves:
on gpt-5-nano most wrong-course cases flip between NEW and WRONG_COURSE on
identical input. This probe runs every wrong-course and guard case N times and
reports how often each fires, so a change can be judged against the spread rather
than a single sample.

False positives are the number that matters — a guard firing WRONG_COURSE even
once is a release blocker, while low recall is an accepted trade. See README.md.

Usage:
    uv run --project faq_automation python -m faq_automation.evals.probe_wrong_course
    uv run --project faq_automation python -m faq_automation.evals.probe_wrong_course gpt-5-nano 5
"""

import os
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from faq_automation.evals.runner import _load_env

_load_env()

from openai import OpenAI

from faq_automation.rag_agent import FAQAgent, DEFAULT_MODEL
from faq_automation.evals import flex
from faq_automation.evals.cases import CASES


def select_cases():
    """Every case written for the wrong-course decision, positive and guard."""
    cases = []
    for case in CASES:
        if 'wrong-course' in case.tags or 'wrong-course-guard' in case.tags:
            cases.append(case)
    return cases


def build_agents(cases, api_key, model):
    """One agent per course, reused across that course's cases."""
    agents = {}
    for case in cases:
        if case.course not in agents:
            agents[case.course] = FAQAgent(
                Path('_questions') / case.course,
                api_key,
                model,
                questions_dir=Path('_questions'),
            )
    return agents


def run_probe(model=DEFAULT_MODEL, repeats=5):
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    cases = select_cases()
    agents = build_agents(cases, api_key, model)
    client = OpenAI(api_key=api_key)

    jobs = []
    for case in cases:
        for _ in range(repeats):
            jobs.append(case)

    print(f"Probing {len(cases)} cases x {repeats} repeats on {model} ({len(jobs)} requests)")

    def run(case):
        messages = agents[case.course].build_messages(case.question, case.answer)
        try:
            decision = flex.request(client, messages, model)
            return case, decision.action, decision.suggested_course
        except Exception as e:
            print(f"  [error] issue #{case.issue_number}: {type(e).__name__}: {e}")
            return case, f'ERROR:{type(e).__name__}', None

    with ThreadPoolExecutor(max_workers=flex.MAX_WORKERS) as pool:
        results = list(pool.map(run, jobs))

    by_case = {}
    for case, action, suggested in results:
        key = (case.issue_number, case.question[:45])
        if key not in by_case:
            by_case[key] = {'case': case, 'actions': Counter(), 'suggested': Counter()}
        by_case[key]['actions'][action] += 1
        if suggested:
            by_case[key]['suggested'][suggested] += 1

    print(f"\n{'='*78}")
    print(f"MODEL: {model}   repeats: {repeats}")
    print(f"{'='*78}")

    recall_hits = 0
    recall_total = 0
    fp_hits = 0
    fp_total = 0

    print("\n-- wrong-course cases (want WRONG_COURSE) --")
    for row in by_case.values():
        case = row['case']
        if 'wrong-course' not in case.tags:
            continue
        fires = row['actions']['WRONG_COURSE']
        recall_hits += fires
        recall_total += repeats
        print(f"  #{case.issue_number:<4} {fires}/{repeats} WRONG_COURSE  "
              f"{dict(row['actions'])} sugg={dict(row['suggested'])}")
        print(f"        {case.question[:70]}")

    print("\n-- guard cases (must NEVER be WRONG_COURSE) --")
    for row in by_case.values():
        case = row['case']
        if 'wrong-course-guard' not in case.tags:
            continue
        fires = row['actions']['WRONG_COURSE']
        fp_hits += fires
        fp_total += repeats
        flag = '  <-- FALSE POSITIVE' if fires else ''
        print(f"  {fires}/{repeats} WRONG_COURSE  {dict(row['actions'])}{flag}")
        print(f"        {case.question[:70]}")

    print(f"\nrecall         : {recall_hits}/{recall_total}")
    print(f"false positives: {fp_hits}/{fp_total}")

    return fp_hits == 0


if __name__ == '__main__':
    model = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    repeats = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    clean = run_probe(model=model, repeats=repeats)
    sys.exit(0 if clean else 1)
