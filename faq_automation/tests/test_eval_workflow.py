"""Contract checks for the manually dispatched full RAG evaluation."""

from pathlib import Path

import yaml

from faq_automation.evals.runner import _prepare_eval_course_copy


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


def test_eval_course_copy_restores_historical_faq_after_hiding_current_doc(tmp_path):
    source = tmp_path / "source"
    section = source / "module-2-homework"
    section.mkdir(parents=True)
    current_file = section / "002_8af59cb98f_current.md"
    current_file.write_text("current corrected answer", encoding="utf-8")
    historical_content = "---\nid: 8af59cb98f\n---\n\nold answer\n"
    historical_path = "module-2-homework/002_8af59cb98f_original.md"
    target = tmp_path / "copy"

    removed_paths = _prepare_eval_course_copy(
        source,
        target,
        remove_doc_ids=["8af59cb98f"],
        historical_files=[(historical_path, historical_content)],
    )

    assert current_file.exists()
    assert current_file.relative_to(source) in removed_paths
    assert not (target / current_file.relative_to(source)).exists()
    assert (target / historical_path).read_text(encoding="utf-8") == historical_content
