"""Contract checks for the manually dispatched full RAG evaluation."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]


def test_full_rag_eval_is_available_as_a_manual_workflow_dispatch():
    workflow = yaml.load(
        (ROOT / ".github/workflows/test-faq-automation.yml").read_text(
            encoding="utf-8"
        ),
        Loader=yaml.BaseLoader,
    )

    assert "workflow_dispatch" in workflow["on"]
    assert workflow["jobs"]["rag-eval"]["if"] == (
        "github.event_name == 'workflow_dispatch' && inputs.run_rag_eval"
    )
    assert workflow["jobs"]["rag-eval"]["env"]["OPENAI_API_KEY"] == (
        "${{ secrets.OPENAI_API_KEY }}"
    )
    assert "faq_automation.evals.runner" in (
        workflow["jobs"]["rag-eval"]["steps"][-1]["run"]
    )
