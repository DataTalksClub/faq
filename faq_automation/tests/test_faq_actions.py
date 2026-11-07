"""
Unit tests for FAQ automation actions
"""

import pytest
from faq_automation.actions import (
    _slugify,
    create_new_faq_file,
    generate_duplicate_comment,
    generate_duplicate_submission_comment,
    generate_pr_body,
    find_duplicate_submission,
    normalize_issue_title,
    update_existing_faq_file,
)
from faq_automation.core import parse_frontmatter
from faq_automation.rag_agent import FAQDecision


class TestGeneratePRBody:
    """Test the generate_pr_body function"""

    def test_generate_pr_body_new(self):
        """Test PR body generation for NEW action"""
        decision = FAQDecision(
            action='NEW',
            rationale='This is a new question not covered in existing FAQs.',
            document_id='abc123',
            section_rationale='Best fits in general section as it is a course overview question.',
            section_id='general',
            order=-1,
            question='How long does the course take?',
            proposed_content='The course typically takes 4 months to complete.',
            filename_slug='how-long-does-course-take',
            warnings=[]
        )

        pr_body = generate_pr_body(decision, 42, 'machine-learning-zoomcamp')

        assert '✨ FAQ NEW' in pr_body
        assert 'machine-learning-zoomcamp' in pr_body
        assert 'general' in pr_body
        assert '#42' in pr_body
        assert 'How long does the course take?' in pr_body
        assert 'how-long-does-course-take' in pr_body

    def test_generate_pr_body_update(self):
        """Test PR body generation for UPDATE action"""
        decision = FAQDecision(
            action='UPDATE',
            rationale='Adds additional troubleshooting steps to existing FAQ.',
            document_id='xyz789',
            section_rationale='Module 1 docker troubleshooting.',
            section_id='module-1',
            order=15,
            question='Docker connection issues?',
            proposed_content='Updated answer with more troubleshooting.',
            filename_slug=None,
            warnings=['Sort order may conflict with existing entry']
        )

        pr_body = generate_pr_body(decision, 99, 'machine-learning-zoomcamp')

        assert '📝 FAQ UPDATE' in pr_body
        assert 'module-1' in pr_body
        assert '#99' in pr_body
        assert 'xyz789' in pr_body
        assert '⚠️ Warnings' in pr_body
        assert 'Sort order may conflict' in pr_body


class TestGenerateDuplicateComment:
    """Test the generate_duplicate_comment function"""

    def test_generate_duplicate_comment(self):
        """Test duplicate comment generation"""
        decision = FAQDecision(
            action='DUPLICATE',
            rationale='This question is already fully answered in existing FAQ.',
            document_id='existing123',
            section_rationale='General course questions.',
            section_id='general',
            order=-1,
            question='When does the course start?',
            proposed_content=None,
            filename_slug=None,
            warnings=[]
        )

        comment = generate_duplicate_comment(
            decision,
            'machine-learning-zoomcamp',
            site_url='https://datatalks.club/faq'
        )

        assert '🔄 Duplicate FAQ Entry' in comment
        assert 'When does the course start?' in comment
        assert 'existing123' in comment
        assert 'https://datatalks.club/faq/machine-learning-zoomcamp.html#existing123' in comment
        assert '_questions/machine-learning-zoomcamp/general/' in comment


class TestSlugify:
    """Test the _slugify helper function"""

    def test_basic_slugify(self):
        """Test basic text to slug conversion"""
        assert _slugify("How do I install Docker?") == "how-do-i-install-docker"

    def test_special_characters_removed(self):
        """Test that special characters are stripped"""
        assert _slugify("What's the deadline (2024)?") == "whats-the-deadline-2024"

    def test_max_length(self):
        """Test slug truncation at max_length"""
        long = "this is a very long question that exceeds the maximum length"
        result = _slugify(long, max_length=20)
        assert len(result) <= 20
        assert not result.endswith('-')

    def test_multiple_spaces(self):
        """Test multiple spaces collapse to single hyphen"""
        assert _slugify("too   many    spaces") == "too-many-spaces"

    def test_empty_string(self):
        """Test empty input"""
        assert _slugify("") == ""


def test_create_new_faq_file_sanitizes_model_provided_slug(tmp_path):
    section_dir = tmp_path / "module-4"
    section_dir.mkdir()
    decision = FAQDecision(
        action="NEW",
        rationale="New evaluation question.",
        document_id="unused",
        section_rationale="Evaluation metrics belong in Module 4.",
        section_id="module-4",
        order=1,
        question="Why can MRR improve while Hit Rate stays the same?",
        proposed_content="MRR also considers the first relevant result's rank.",
        filename_slug="mrr-vs-hit-rate}>" + "unexpected-model-output-" * 100,
        warnings=[],
    )

    faq_file = create_new_faq_file(tmp_path, {}, decision)
    slug = faq_file.stem.split("_", maxsplit=2)[2]

    assert faq_file.parent == section_dir
    assert len(slug) <= 50
    assert slug == _slugify(decision.filename_slug)


def test_create_new_faq_file_creates_missing_section_dir(tmp_path):
    section_dir = tmp_path / "04-devops-homework"
    assert not section_dir.exists()
    decision = FAQDecision(
        action="NEW",
        rationale="First entry in a new homework section.",
        document_id="unused",
        section_rationale="Unit 4 homework question.",
        section_id="04-devops-homework",
        order=-1,
        question="Why does my Grafana alert stay Normal?",
        proposed_content="Check the Grafana logs for rule evaluator errors.",
        filename_slug="grafana-alert-stays-normal",
        warnings=[],
    )

    faq_file = create_new_faq_file(tmp_path, {}, decision)

    assert section_dir.is_dir()
    assert faq_file.parent == section_dir
    assert faq_file.exists()
    assert faq_file.name.startswith("001_")


def test_normalize_issue_title_collapses_whitespace_and_rejects_empty():
    assert normalize_issue_title("  How do I\nuse uv?  ") == "How do I use uv?"
    assert len(normalize_issue_title("x" * 300)) == 256
    with pytest.raises(ValueError, match="cannot be empty"):
        normalize_issue_title(" \n ")


def test_find_duplicate_submission_matches_normalized_open_faq_question():
    related_issues = [
        {
            "number": 523,
            "title": "[FAQ] API accepts invalid input",
            "labels": [],
            "body": """### Course
machine-learning-zoomcamp

### Question
Why does `/predict` accept invalid categorical values?

### Answer
The request model checks types but not all semantic values.
""",
        },
        {
            "number": 524,
            "title": "[FAQ] API accepts invalid input",
            "labels": ["faq-proposal"],
            "body": "### Course\nmachine-learning-zoomcamp\n",
        },
    ]

    duplicate = find_duplicate_submission(
        "Why does `/predict` accept invalid categorical values!",
        "machine-learning-zoomcamp",
        524,
        related_issues,
    )

    assert duplicate["number"] == 523
    comment = generate_duplicate_submission_comment(duplicate)
    assert "issue #523" in comment
    assert "separate FAQ PRs" in comment


def test_find_duplicate_submission_does_not_match_on_title_when_questions_differ():
    duplicate = find_duplicate_submission(
        "When running `uv run python script.py`, why does VIRTUAL_ENV not match the project environment path? How can I resolve this?",
        "machine-learning-zoomcamp",
        534,
        [
            {
                "number": 531,
                "title": "### How to fix uv warning: VIRTUAL_ENV does not match the project environment path",
                "body": """### Course
machine-learning-zoomcamp

When running scripts with `uv run`, I get a virtual environment warning.

**Answer:**
This warning occurs because `uv` selects the project environment by default.
""",
            }
        ],
        issue_title="How to fix uv warning: VIRTUAL_ENV does not match the project environment path",
    )

    assert duplicate is None


def test_find_duplicate_submission_requires_course_evidence():
    duplicate = find_duplicate_submission(
        "Why does `/predict` accept invalid categorical values?",
        "machine-learning-zoomcamp",
        524,
        [
            {
                "number": 523,
                "title": "[FAQ] API accepts invalid input",
                "labels": ["faq-proposal"],
                "body": """### Question
Why does `/predict` accept invalid categorical values?

### Answer
The request model checks types but not all semantic values.
""",
            }
        ],
    )

    assert duplicate is None


def test_find_duplicate_submission_does_not_match_other_course():
    duplicate = find_duplicate_submission(
        "How do I install dependencies with uv?",
        "machine-learning-zoomcamp",
        100,
        [
            {
                "number": 99,
                "title": "[FAQ] How do I install dependencies with uv?",
                "labels": ["faq-proposal"],
                "body": """### Course
llm-zoomcamp
### Question
How do I install dependencies with uv?
### Answer
Run `uv sync`.
""",
            }
        ],
    )

    assert duplicate is None


def test_find_duplicate_submission_normalizes_known_course_aliases():
    duplicate = find_duplicate_submission(
        "Do I need to scale features before training a decision tree?",
        "machine-learning-zoomcamp",
        544,
        [
            {
                "number": 543,
                "title": "[FAQ] Scaling for trees",
                "labels": ["faq-proposal"],
                "body": """### Course
ml-zoomcamp

### Question
Do I need to scale features before training a decision tree?

### Answer
No. A monotonic scale change preserves feature ordering.
""",
            }
        ],
    )

    assert duplicate["number"] == 543


def test_update_existing_faq_file_preserves_id_and_moves_to_section_end(tmp_path):
    source_dir = tmp_path / "module-1"
    target_dir = tmp_path / "module-2-homework"
    source_dir.mkdir()
    target_dir.mkdir()
    source = source_dir / "002_abc1234567_old-title.md"
    source.write_text(
        "---\nid: abc1234567\nquestion: Old question\nsort_order: 2\n---\n\nOld answer.\n",
        encoding="utf-8",
    )
    (target_dir / "005_def1234567_existing.md").write_text(
        "---\nid: def1234567\nquestion: Existing\nsort_order: 5\n---\n\nExisting.\n",
        encoding="utf-8",
    )
    doc_index = {"abc1234567": source}
    decision = FAQDecision(
        action="UPDATE",
        rationale="This question updates the existing entry.",
        document_id="abc1234567",
        section_rationale="The question is specific to homework.",
        section_id="module-2-homework",
        order=1,
        question="Updated question?",
        proposed_content="Updated answer.\n",
        filename_slug=None,
        warnings=[],
    )

    result = update_existing_faq_file(tmp_path, doc_index, decision)

    assert result == target_dir / "006_abc1234567_old-title.md"
    assert not source.exists()
    metadata, answer = parse_frontmatter(result.read_text(encoding="utf-8"))
    assert metadata["id"] == "abc1234567"
    assert metadata["question"] == "Updated question?"
    assert metadata["sort_order"] == 6
    assert answer == "Updated answer."
    assert doc_index["abc1234567"] == result


def test_update_existing_faq_file_keeps_order_for_in_place_update(tmp_path):
    section_dir = tmp_path / "module-1"
    section_dir.mkdir()
    source = section_dir / "002_abc1234567_old-title.md"
    source.write_text(
        "---\nid: abc1234567\nquestion: Old question\nsort_order: 2\n---\n\nOld answer.\n",
        encoding="utf-8",
    )
    decision = FAQDecision(
        action="UPDATE",
        rationale="This question updates the existing entry.",
        document_id="abc1234567",
        section_rationale="Same section.",
        section_id="module-1",
        order=9,
        question="Updated question?",
        proposed_content="Updated answer.\n",
        filename_slug=None,
        warnings=[],
    )

    result = update_existing_faq_file(tmp_path, {"abc1234567": source}, decision)

    metadata, _ = parse_frontmatter(result.read_text(encoding="utf-8"))
    assert result == source
    assert metadata["sort_order"] == 2


def test_generate_pr_body_uses_actual_file_order():
    decision = FAQDecision(
        action="UPDATE",
        rationale="Update an existing entry.",
        document_id="abc1234567",
        section_rationale="Homework-specific guidance.",
        section_id="module-2-homework",
        order=3,
        question="Why does the result differ?",
        proposed_content="Check the train split.",
        filename_slug=None,
        warnings=[],
    )

    body = generate_pr_body(decision, 548, "machine-learning-zoomcamp", actual_sort_order=2)

    assert "**Sort Order**: 2" in body
