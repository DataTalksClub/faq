"""
Unit tests for CLI issue body parsing
"""

import pytest
from faq_automation.cli import (
    build_invalid_proposal_decision,
    parse_full_issue_body,
    validate_faq_decision,
)
from faq_automation.core import normalize_course_id
from faq_automation.rag_agent import FAQDecision


class TestParseFullIssueBody:
    """Test the parse_full_issue_body function"""

    def test_parse_full_issue_body_simple(self):
        """Test parsing simple issue body with all fields"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
How do I install dependencies?

### Answer
Run: pip install -r requirements.txt
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "How do I install dependencies?"
        assert "pip install -r requirements.txt" in answer

    def test_parse_full_issue_body_multiline(self):
        """Test parsing issue body with multiline content"""
        issue_body = """### Course
data-engineering-zoomcamp

### Question
How do I set up
the development environment
for this project?

### Answer
First, clone the repository:
```bash
git clone https://github.com/...
```

Then install dependencies:
```bash
pip install -r requirements.txt
```
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "data-engineering-zoomcamp"
        assert "set up" in question
        assert "development environment" in question
        assert "git clone" in answer
        assert "pip install" in answer

    def test_parse_full_issue_body_with_checklist(self):
        """Test parsing with checklist section that should be ignored"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
What is the deadline?

### Answer
The deadline is March 1st.

### Checklist
- [x] Searched existing FAQs
- [x] Accurate information
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "What is the deadline?"
        assert answer == "The deadline is March 1st."
        assert "Checklist" not in answer

    def test_parse_full_issue_body_missing_course(self):
        """Test parsing with missing course raises error"""
        issue_body = """### Question
Some question

### Answer
Some answer
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_missing_question(self):
        """Test parsing with missing question raises error"""
        issue_body = """### Course
machine-learning-zoomcamp

### Answer
Some answer
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_with_markdown_headings_in_content(self):
        """Test parsing when question/answer contain ### headings (issue #169)"""
        issue_body = """### Course

data-engineering-zoomcamp

### Question

### 04-analytics-engineering

When setting up **dbt cloud** environment, we need to create a connection to **BigQuery**.
If you are still **not able to create JSON key** for your BQ service account, **DON'T!**

### Answer

The only solution is to bruteforce delete the iam.disableServiceAccountKeyCreation
1. Add yourself "Service Account Key Admin" role.
2. Run:
```bash
gcloud org-policies delete iam.disableServiceAccountKeyCreation --organization=[your-org-id]
```

### Checklist

- [x] I have searched existing FAQs and this question is not already answered
- [x] The answer provides accurate, helpful information
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "data-engineering-zoomcamp"
        assert "04-analytics-engineering" in question
        assert "dbt cloud" in question
        assert "gcloud org-policies delete" in answer
        assert "Checklist" not in answer

    def test_parse_full_issue_body_missing_answer(self):
        """Test parsing with missing answer raises error"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
Some question
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_empty_answer(self):
        """A present-but-empty section is treated as missing and raises"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
Some question

### Answer

### Checklist
- [x] done
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_out_of_order(self):
        """Sections may appear in any order"""
        issue_body = """### Answer
Run pip install.

### Course
machine-learning-zoomcamp

### Question
How do I install?
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "How do I install?"
        assert answer == "Run pip install."

    def test_parse_full_issue_body_crlf_line_endings(self):
        """Windows/GitHub CRLF line endings parse the same as LF"""
        issue_body = (
            "### Course\r\nmachine-learning-zoomcamp\r\n\r\n"
            "### Question\r\nHow do I install?\r\n\r\n"
            "### Answer\r\nRun pip install.\r\n"
        )

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "How do I install?"
        assert answer == "Run pip install."

    def test_parse_full_issue_body_accepts_two_level_field_headings(self):
        """A valid proposal remains valid when its field headings use ##."""
        issue_body = """## Course
machine-learning-zoomcamp

## Question
Why does the Homework 5 prediction differ?

## Answer
Run `uv sync --locked` in the homework directory.
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "Why does the Homework 5 prediction differ?"
        assert "uv sync --locked" in answer


def test_incomplete_proposal_result_explains_how_to_reopen():
    decision = build_invalid_proposal_decision(521)

    assert decision["action"] == "INVALID_PROPOSAL"
    assert decision["issue_number"] == 521
    assert "course, question, or answer" in decision["comment"]
    assert "reopen it" in decision["comment"]


def test_normalize_course_id_maps_observed_ml_zoomcamp_alias():
    assert normalize_course_id(" ML-Zoomcamp ") == "machine-learning-zoomcamp"


def _decision(**overrides):
    values = {
        "action": "NEW",
        "rationale": "This is a new question.",
        "document_id": "unused12345",
        "section_rationale": "It belongs in module 1.",
        "section_id": "module-1",
        "order": -1,
        "question": "How do I install dependencies?",
        "proposed_content": "Run `uv sync`.\n",
        "filename_slug": "install-dependencies",
        "warnings": [],
    }
    values.update(overrides)
    return FAQDecision(**values)


def _course_dir(tmp_path):
    course_dir = tmp_path / "test-course"
    course_dir.mkdir()
    (course_dir / "_metadata.yaml").write_text(
        "course: test-course\ncourse_name: Test Course\nsections:\n  - id: module-1\n    name: Module 1\n",
        encoding="utf-8",
    )
    return course_dir


def test_validate_faq_decision_rejects_empty_question(tmp_path):
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_faq_decision(_decision(question=" \n "), _course_dir(tmp_path), {})


def test_validate_faq_decision_rejects_empty_new_answer(tmp_path):
    with pytest.raises(ValueError, match="non-empty answer"):
        validate_faq_decision(
            _decision(proposed_content="  "),
            _course_dir(tmp_path),
            {},
        )


def test_validate_faq_decision_rejects_invalid_section(tmp_path):
    with pytest.raises(ValueError, match="Unknown FAQ section"):
        validate_faq_decision(
            _decision(section_id="module-99"),
            _course_dir(tmp_path),
            {},
        )


def test_validate_faq_decision_rejects_update_to_unknown_document(tmp_path):
    with pytest.raises(ValueError, match="unknown FAQ document"):
        validate_faq_decision(
            _decision(action="UPDATE", document_id="missing1234"),
            _course_dir(tmp_path),
            {},
        )
