"""
GitHub Actions integration for FAQ automation

Handles creating PRs, adding comments, and managing issues.
"""

import re
import json
import frontmatter
from pathlib import Path
from typing import Optional

from .core import (
    generate_document_id,
    find_largest_sort_order,
    write_frontmatter,
    find_question_files,
    parse_frontmatter,
)
from .rag_agent import FAQDecision


def _slugify(text: str, max_length: int = 50) -> str:
    """Convert text to a file-system friendly slug."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug).strip('-')
    return slug[:max_length].rstrip('-')


def _file_order(faq_file: Path) -> Optional[int]:
    """Return the leading sort_order of a `NNN_id_slug.md` file, or None."""
    head = faq_file.name.split('_', maxsplit=1)[0]
    if head.isdigit():
        return int(head)
    return None


def _shift_section_files(section_dir: Path, from_order: int) -> None:
    """
    Rename all files in section_dir with sort_order >= from_order,
    bumping each up by 1 to make room for a new entry at from_order.
    """
    files_to_shift = []
    for f in section_dir.glob('*.md'):
        order = _file_order(f)
        if order is not None and order >= from_order:
            files_to_shift.append((order, f))

    # Shift from highest to lowest to avoid temporary collisions
    for order, f in sorted(files_to_shift, reverse=True):
        new_order = order + 1
        rest = f.name.split('_', maxsplit=1)[1]
        new_path = f.parent / f'{new_order:03d}_{rest}'

        # Update sort_order in frontmatter
        content = f.read_text(encoding='utf-8')
        post = frontmatter.loads(content)
        post.metadata['sort_order'] = new_order
        f.write_text(frontmatter.dumps(post), encoding='utf-8')

        f.rename(new_path)


def create_new_faq_file(
    course_dir: Path,
    doc_index: dict,
    faq_decision: FAQDecision
) -> Path:
    """
    Create a new FAQ file based on the decision.

    If the agent chose a specific sort_order that collides with an existing
    entry, existing entries from that position onward are shifted up by one
    to make room. If order is -1, the file is appended to the end.

    Args:
        course_dir: Path to course directory
        doc_index: Dictionary mapping document IDs to file paths
        faq_decision: FAQDecision object from the agent

    Returns:
        Path to the created file
    """
    # Generate document ID
    doc_id = generate_document_id(
        faq_decision.question,
        faq_decision.proposed_content,
        doc_index
    )

    sort_order = faq_decision.order
    doc_slug = _slugify(faq_decision.filename_slug or faq_decision.question)
    faq_section = faq_decision.section_id
    section_dir = course_dir / faq_section

    # If order is -1, append to end of section
    if sort_order == -1:
        sort_order = find_largest_sort_order(section_dir)
    else:
        # Check for collision and shift existing entries to make room
        existing_orders = set()
        for f in section_dir.glob('*.md'):
            order = _file_order(f)
            if order is not None:
                existing_orders.add(order)
        if sort_order in existing_orders:
            _shift_section_files(section_dir, sort_order)

    # Create frontmatter
    fm = {
        'id': doc_id,
        'question': faq_decision.question,
        'sort_order': sort_order,
    }

    # Create file
    filename = f'{sort_order:03d}_{doc_id}_{doc_slug}.md'
    f_out = section_dir / filename
    write_frontmatter(f_out, fm, faq_decision.proposed_content)

    return f_out


def update_existing_faq_file(
    course_dir: Path,
    doc_index: dict,
    faq_decision: FAQDecision
) -> Path:
    """
    Update an existing FAQ file based on the decision

    Args:
        course_dir: Path to course directory
        doc_index: Dictionary mapping document IDs to file paths
        faq_decision: FAQDecision object from the agent

    Returns:
        Path to the updated file
    """
    doc_id = faq_decision.document_id
    f_out = doc_index[doc_id]

    # Read existing frontmatter
    content = f_out.read_text(encoding='utf8')
    fm, _ = parse_frontmatter(content)

    # Update question
    fm['question'] = faq_decision.question

    # Write updated content
    write_frontmatter(f_out, fm, faq_decision.proposed_content)

    return f_out


def generate_pr_body(
    faq_decision: FAQDecision,
    issue_number: int,
    course_name: str
) -> str:
    """
    Generate the PR body text

    Args:
        faq_decision: FAQDecision object from the agent
        issue_number: GitHub issue number
        course_name: Name of the course

    Returns:
        Formatted PR body text
    """
    action_emoji = {
        'NEW': '✨',
        'UPDATE': '📝',
    }

    body = f"""## {action_emoji[faq_decision.action]} FAQ {faq_decision.action}

**Course**: {course_name}
**Section**: {faq_decision.section_id} ({faq_decision.section_rationale})
**Related Issue**: #{issue_number}

### Question
{faq_decision.question}

### Decision Rationale
{faq_decision.rationale}

### Placement Details
- **Section ID**: `{faq_decision.section_id}`
- **Sort Order**: {faq_decision.order if faq_decision.order != -1 else "End of section"}
"""

    if faq_decision.action == 'NEW':
        body += f"- **Filename Slug**: `{faq_decision.filename_slug}`\n"

    if faq_decision.action == 'UPDATE':
        body += f"- **Document ID**: `{faq_decision.document_id}`\n"

    if faq_decision.warnings:
        body += "\n### ⚠️ Warnings\n"
        for warning in faq_decision.warnings:
            body += f"- {warning}\n"

    body += "\n---\n"
    body += "\n🤖 Generated by FAQ Bot\n"

    return body


def generate_duplicate_comment(
    faq_decision: FAQDecision,
    course_name: str,
    site_url: Optional[str] = None
) -> str:
    """
    Generate comment for DUPLICATE decisions

    Args:
        faq_decision: FAQDecision object from the agent
        course_name: Name of the course
        site_url: Base URL for the generated site (optional)

    Returns:
        Formatted comment text
    """
    comment = f"""## 🔄 Duplicate FAQ Entry

Thank you for your proposal! After analyzing existing FAQs, this question appears to already be covered.

### Matching FAQ
**Question**: {faq_decision.question}
**Document ID**: `{faq_decision.document_id}`
**Section**: {faq_decision.section_id}

### Rationale
{faq_decision.rationale}

### Where to Find This FAQ
"""

    if site_url:
        comment += f"- **Live Site**: {site_url}/{course_name}.html#{faq_decision.document_id}\n"

    comment += f"- **Source File**: `_questions/{course_name}/{faq_decision.section_id}/`\n"

    comment += "\n---\n"
    comment += "\n🤖 This issue has been automatically closed by FAQ Bot.\n"
    comment += "If you believe this is an error, please reopen and mention a maintainer.\n"

    return comment


def generate_wrong_course_comment(
    faq_decision: FAQDecision,
    course_name: str
) -> str:
    """
    Generate comment for WRONG_COURSE decisions

    Args:
        faq_decision: FAQDecision object from the agent
        course_name: The course the proposal was filed against

    Returns:
        Formatted comment text
    """
    comment = f"""## 📚 Wrong Course

Thank you for your proposal! It was filed against **{course_name}**, but the question is about a different course, so it can't be added here.

### Rationale
{faq_decision.rationale}
"""

    if faq_decision.suggested_course:
        comment += f"\n### Where This Belongs\nThis looks like a **{faq_decision.suggested_course}** question."
        comment += " Please open a new proposal and pick that course in the **Course** dropdown.\n"
    else:
        comment += "\nPlease open a new proposal and pick the right course in the **Course** dropdown.\n"

    comment += "\n---\n"
    comment += "\n🤖 This issue has been automatically closed by FAQ Bot.\n"
    comment += "If the course was right after all, please reopen and mention a maintainer.\n"

    return comment


def get_file_changes_summary(action: str, file_path: Path, course_dir: Path) -> dict:
    """
    Generate a summary of file changes for logging

    Args:
        action: NEW or UPDATE
        file_path: Path to the modified file
        course_dir: Base course directory

    Returns:
        Dictionary with change summary
    """
    relative_path = file_path.relative_to(course_dir.parent)

    return {
        'action': action,
        'file': relative_path.as_posix(),  # Use forward slashes for cross-platform compatibility
        'filename': file_path.name,
    }
