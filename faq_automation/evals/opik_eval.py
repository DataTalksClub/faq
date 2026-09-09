"""Opik port of the generation evals (datasets + experiments).

ADDITIVE: runner.py, cases.py and the rest of the framework are untouched.
To go back, delete this file and run the local runner instead:
  uv run --project faq_automation python -m faq_automation.evals.runner

What this adds:
  - push the eval cases to an Opik dataset (once)
  - run any subset as an Opik experiment with deterministic metrics
    (action match + placement match, no judge model, no extra cost)
  - before/after comparison via experiment_config (e.g. num_results 1 vs 5)

Traces attach to the experiment automatically: the task calls
FAQAgent.process_proposal, which is @track-ed in rag_agent.py.

Usage:
  # one-time: push 6 Friday-demo cases to Cloud
  OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \\
    OPIK_PROJECT_NAME=faq-automation-ci OPIK_API_KEY=... \\
    uv run --project faq_automation python -m faq_automation.evals.opik_eval --push-dataset

  # before/after (needs OPENAI_API_KEY too)
  uv run --project faq_automation python -m faq_automation.evals.opik_eval \\
    --experiment friday-before --num-results 1
  uv run --project faq_automation python -m faq_automation.evals.opik_eval \\
    --experiment friday-after --num-results 5
"""

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

from faq_automation.evals.cases import CASES
from faq_automation.evals.runner import evaluate, get_section_sort_orders
from faq_automation.rag_agent import DEFAULT_MODEL, FAQAgent

# Small, cheap Friday-demo subset: mixed actions/courses, one known-hard
# placement case (187, human had to move it) for the error-analysis beat.
DEMO_CASE_IDS = [289, 295, 300, 330, 316, 187]


def _item(case):
    return {
        "course": case.course,
        "case_id": case.case_id,
        "question": case.question,
        "answer": case.answer,
        "expected_action": case.expected_action,
        "expected_section": case.expected_section or "",
        "description": case.description,
        "relevant_doc_id": case.relevant_doc_id,
        "hidden_doc_ids": list(case.hidden_doc_ids),
    }


def push_dataset(project, name, cases):
    from opik import Opik

    client = Opik(project_name=project)
    try:
        dataset = client.get_dataset(name=name)
    except Exception:
        dataset = client.create_dataset(name=name)
    existing = len(dataset.get_items() or [])
    if existing:
        print(f"dataset {name!r}: {existing} items already there, skipping insert")
        return dataset
    dataset.insert([_item(c) for c in cases])
    print(f"dataset {name!r}: inserted {len(cases)} items")
    return dataset


class _Agents:
    """Mirrors runner.run_all agent prep (leave-one-out) without touching it."""

    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        self.cache = {}

    def get(self, course, remove_doc_ids):
        key = (course, tuple(sorted(remove_doc_ids)))
        if key not in self.cache:
            course_dir = Path("_questions") / course
            tmp = None
            if remove_doc_ids:
                tmp = Path(tempfile.mkdtemp()) / course
                shutil.copytree(course_dir, tmp)
                for f in tmp.glob("*/*.md"):
                    parts = f.name.split("_", maxsplit=2)
                    if len(parts) >= 2 and parts[1] in remove_doc_ids:
                        f.unlink()
                course_dir = tmp
            agent = FAQAgent(course_dir, self.api_key, self.model,
                             questions_dir=Path("_questions"))
            self.cache[key] = (agent, get_section_sort_orders(course_dir))
        return self.cache[key]


def _field(item, name, default=""):
    if isinstance(item, dict):
        return item.get(name, default)
    return getattr(item, name, default)


def make_task(agents, num_results):
    def task(item):
        course = _field(item, "course")
        remove = set(_field(item, "hidden_doc_ids", []) or [])
        if _field(item, "expected_action") == "NEW" and _field(item, "relevant_doc_id"):
            remove.add(_field(item, "relevant_doc_id"))
        agent, orders = agents.get(course, remove)
        decision = agent.process_proposal(
            _field(item, "question"), _field(item, "answer"), num_results=num_results)
        # Full-fidelity scoring via the framework's own predicates.
        from faq_automation.evals.cases import EvalCase

        case = EvalCase(course=course, case_id=int(_field(item, "case_id", 0)),
                        question=_field(item, "question"), answer=_field(item, "answer"),
                        expected_action=_field(item, "expected_action"),
                        expected_section=_field(item, "expected_section") or None,
                        relevant_doc_id=_field(item, "relevant_doc_id"),
                        hidden_doc_ids=list(_field(item, "hidden_doc_ids", []) or []))
        row = evaluate(case, decision, orders)
        return {
            "action": decision.action,
            "section": decision.section_id,
            "expected_action": case.expected_action,
            "expected_section": case.expected_section or "",
            "checks_passed": sum(1 for r in row["results"] if r["passed"]),
            "checks_total": len(row["results"]),
        }

    return task


def _metrics():
    from opik.evaluation.metrics import base_metric, score_result

    class ActionMatch(base_metric.BaseMetric):
        def score(self, action, expected_action, **ignored):
            ok = action == expected_action
            return score_result.ScoreResult(
                value=1.0 if ok else 0.0, name=self.name,
                reason=f"got {action}, expected {expected_action}")

    class PlacementMatch(base_metric.BaseMetric):
        def score(self, section, expected_section="", **ignored):
            if not expected_section:
                return score_result.ScoreResult(
                    value=1.0, name=self.name, reason="no placement under test")
            ok = section == expected_section
            return score_result.ScoreResult(
                value=1.0 if ok else 0.0, name=self.name,
                reason=f"got {section}, expected {expected_section}")

    return [ActionMatch(name="action_match"), PlacementMatch(name="placement_match")]


def run_experiment(project, dataset_name, experiment, num_results, model, case_ids):
    from opik import Opik
    from opik.evaluation import evaluate as opik_evaluate

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY not set")
    client = Opik(project_name=project)
    dataset = client.get_dataset(name=dataset_name)
    agents = _Agents(api_key, model)
    result = opik_evaluate(
        dataset=dataset,
        task=make_task(agents, num_results),
        scoring_metrics=_metrics(),
        experiment_name=experiment,
        experiment_config={"num_results": num_results, "model": model},
        project_name=project,
    )
    print(f"\nexperiment {experiment!r} done: {result}")
    return result


def main():
    parser = argparse.ArgumentParser(description="Opik port of the generation evals")
    parser.add_argument("--project", default=os.environ.get(
        "OPIK_PROJECT_NAME", "faq-automation-ci"))
    parser.add_argument("--dataset", default="faq-triage-friday")
    parser.add_argument("--push-dataset", action="store_true")
    parser.add_argument("--experiment", default="friday-before")
    parser.add_argument("--num-results", type=int, default=5)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--case", type=int, action="append", dest="cases",
                        help="only these case_ids (repeatable)")
    args = parser.parse_args()

    cases = CASES
    wanted = args.cases or DEMO_CASE_IDS
    cases = [c for c in cases if c.case_id in wanted]
    if not cases:
        sys.exit(f"no cases match {wanted}")

    if args.push_dataset:
        push_dataset(args.project, args.dataset, cases)
        return

    run_experiment(args.project, args.dataset, args.experiment,
                   args.num_results, args.model, wanted)


if __name__ == "__main__":
    main()
