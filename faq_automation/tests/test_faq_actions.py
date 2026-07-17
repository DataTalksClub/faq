"""
Unit tests for FAQ automation actions
"""

import pytest
from faq_automation.actions import (
    _slugify,
    create_new_faq_file,
    generate_duplicate_comment,
    generate_pr_body,
)
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
