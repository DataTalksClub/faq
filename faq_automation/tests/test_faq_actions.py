"""
Unit tests for FAQ automation actions
"""

import pytest
from faq_automation.actions import generate_pr_body, generate_duplicate_comment
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
