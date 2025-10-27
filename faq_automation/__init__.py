"""
FAQ Automation Module

Provides tools for automated FAQ maintenance using RAG and LLM-based triage.
"""

from .core import (
    parse_metadata,
    parse_frontmatter,
    write_frontmatter,
    read_metadata,
    read_questions,
    find_question_files,
    generate_document_id,
    find_largest_sort_order,
)

from .rag_agent import (
    FAQDecision,
    process_faq_proposal,
)

__all__ = [
    'parse_metadata',
    'parse_frontmatter',
    'write_frontmatter',
    'read_metadata',
    'read_questions',
    'find_question_files',
    'generate_document_id',
    'find_largest_sort_order',
    'FAQDecision',
    'process_faq_proposal',
]
