"""Guard the GitHub workflow's PR, CI, and issue-close paths."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]


def _workflow(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def _steps(workflow):
    return workflow["jobs"]["process-faq-proposal"]["steps"]


def test_faq_automation_runs_when_proposal_label_is_added():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")

    assert workflow["on"]["issues"]["types"] == ["opened", "labeled"]
    assert "github.event.label.name == 'faq-proposal'" in workflow["jobs"]["process-faq-proposal"]["if"]


def test_faq_automation_can_retry_a_specific_open_issue_without_relabeling():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    dispatch = workflow["on"]["workflow_dispatch"]["inputs"]["issue_number"]
    fetch = next(step for step in _steps(workflow) if step.get("name") == "Fetch issue body")

    assert dispatch["type"] == "number"
    assert dispatch["required"] == "true"
    assert "github.event_name == 'workflow_dispatch'" in workflow["jobs"]["process-faq-proposal"]["if"]
    assert "issues.get" in fetch["with"]["script"]
    assert "ISSUE_NUMBER" in workflow["jobs"]["process-faq-proposal"]["env"]


def test_automation_serializes_runs_for_the_same_issue():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")

    assert "faq-automation-${{ inputs.issue_number || github.event.issue.number }}" == workflow["concurrency"]["group"]
    assert workflow["concurrency"]["cancel-in-progress"] == "false"


def test_faq_automation_catches_open_duplicate_submissions():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    fetch = next(step for step in _steps(workflow) if step.get("name") == "Fetch issue body")
    process = next(step for step in _steps(workflow) if step.get("name") == "Process FAQ with AI")

    assert "issues.listForRepo" in fetch["with"]["script"]
    assert "related_issues.json" in fetch["with"]["script"]
    assert "--related-issues-file /tmp/related_issues.json" in process["run"]


def test_duplicate_proposals_close_with_an_explanation():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    step = next(
        step for step in _steps(workflow)
        if step.get("name") == "Handle DUPLICATE_SUBMISSION action"
    )
    script = step["with"]["script"]

    assert "decision.comment" in script
    assert "state: 'closed'" in script
    assert "state_reason: 'not_planned'" in script


def test_faq_prs_dispatch_content_ci_and_link_back_to_issue():
    automation = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    new_update = next(
        step for step in _steps(automation)
        if step.get("name") == "Handle NEW or UPDATE action"
    )
    script = new_update["with"]["script"]
    website = _workflow(ROOT / ".github/workflows/test-website.yml")

    assert "github.rest.pulls.create" in script
    assert "Closes #${issueNumber}" in script
    assert "createWorkflowDispatch" in script
    assert "test-website.yml" in script
    assert "workflow_dispatch" in website["on"]
    assert new_update["env"]["DECISION_JSON"] == "${{ steps.process.outputs.decision }}"
    assert "JSON.parse(process.env.DECISION_JSON)" in script
    assert "const decision = ${{ steps.process.outputs.decision }}" not in script


def test_duplicate_faq_and_wrong_course_paths_close_issue():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    duplicate = next(step for step in _steps(workflow) if step.get("name") == "Handle DUPLICATE action")
    wrong_course = next(step for step in _steps(workflow) if step.get("name") == "Handle WRONG_COURSE action")

    for step in (duplicate, wrong_course):
        script = step["with"]["script"]
        assert "github.rest.issues.createComment" in script
        assert "state: 'closed'" in script


def test_incomplete_proposals_close_with_an_explanation():
    workflow = _workflow(ROOT / ".github/workflows/faq-automation.yml")
    invalid = next(
        step for step in _steps(workflow)
        if step.get("name") == "Handle INVALID_PROPOSAL action"
    )
    script = invalid["with"]["script"]

    assert "decision.comment" in script
    assert "state: 'closed'" in script
    assert "state_reason: 'not_planned'" in script


def test_full_rag_eval_is_manually_dispatchable_with_repo_secret():
    workflow = _workflow(ROOT / ".github/workflows/test-faq-automation.yml")
    rag_eval = workflow["jobs"]["rag-eval"]

    assert "workflow_dispatch" in workflow["on"]
    assert "inputs.run_rag_eval" in rag_eval["if"]
    assert rag_eval["env"]["OPENAI_API_KEY"] == "${{ secrets.OPENAI_API_KEY }}"
    assert "faq_automation.evals.runner" in rag_eval["steps"][-1]["run"]
