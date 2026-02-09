"""
Unit tests for FAQ automation core functions
"""

import pytest
from pathlib import Path
import tempfile
import shutil

from faq_automation.core import (
    parse_frontmatter,
    write_frontmatter,
    generate_document_id,
    keep_relevant,
)


class TestParseFrontmatter:
    """Test the parse_frontmatter function"""

    def test_parse_frontmatter(self):
        """Test parsing YAML frontmatter from markdown"""
        content = """---
id: abc123
question: Test question?
sort_order: 1
---

This is the answer content.
"""
        fm, markdown = parse_frontmatter(content)

        assert fm['id'] == 'abc123'
        assert fm['question'] == 'Test question?'
        assert fm['sort_order'] == 1
        assert markdown == 'This is the answer content.'

    def test_parse_frontmatter_no_frontmatter(self):
        """Test parsing content without frontmatter"""
        content = "Just plain markdown content"
        fm, markdown = parse_frontmatter(content)

        assert fm == {}
        assert markdown == content


class TestWriteFrontmatter:
    """Test the write_frontmatter function"""

    def test_write_frontmatter(self):
        """Test writing frontmatter to a file"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            temp_path = Path(f.name)

        try:
            frontmatter = {
                'id': 'test123',
                'question': 'How to test?',
                'sort_order': 5
            }
            content = 'This is test content.'

            write_frontmatter(temp_path, frontmatter, content)

            # Read back and verify
            written_content = temp_path.read_text()
            assert '---' in written_content
            assert 'id: test123' in written_content
            assert 'question: How to test?' in written_content
            assert 'This is test content.' in written_content
        finally:
            temp_path.unlink()


class TestGenerateDocumentId:
    """Test the generate_document_id function"""

    def test_generate_document_id(self):
        """Test document ID generation"""
        question = "What is machine learning?"
        answer = "Machine learning is a subset of AI..."
        existing_ids = {}

        doc_id = generate_document_id(question, answer, existing_ids)

        assert isinstance(doc_id, str)
        assert len(doc_id) == 10
        assert doc_id.isalnum()

    def test_generate_document_id_collision(self):
        """Test document ID generation with collision"""
        question = "Test question"
        answer = "Test answer"

        # First ID
        existing_ids = {}
        doc_id1 = generate_document_id(question, answer, existing_ids)
        existing_ids[doc_id1] = True

        # Try to generate same ID (should handle collision)
        doc_id2 = generate_document_id(question, answer, existing_ids)

        assert doc_id1 != doc_id2
        assert len(doc_id2) == 10


class TestKeepRelevant:
    """Test the keep_relevant function"""

    def test_keep_relevant(self):
        """Test filtering of search results"""
        results = [
            {
                'course': 'ml-zoomcamp',
                'section': 'General',
                'question': 'Test?',
                'answer': 'Answer',
                'document_id': 'abc123'
            },
            {
                'course': 'ml-zoomcamp',
                'section': 'Module 1',
                'question': 'Test 2?',
                'answer': 'Answer 2',
                'document_id': 'def456'
            }
        ]

        filtered = keep_relevant(results)

        assert len(filtered) == 2
        assert 'course' not in filtered[0]
        assert 'section' not in filtered[0]
        assert 'question' in filtered[0]
        assert 'answer' in filtered[0]
        assert 'document_id' in filtered[0]
