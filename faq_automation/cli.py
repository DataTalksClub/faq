#!/usr/bin/env python3
"""
CLI tool for FAQ automation

Used by GitHub Actions to process FAQ proposals from issues.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path

from .rag_agent import process_faq_proposal, DEFAULT_MODEL
from .core import find_question_files, read_metadata, normalize_course_id
from .actions import (
    create_new_faq_file,
    update_existing_faq_file,
    generate_pr_body,
    generate_duplicate_comment,
    generate_duplicate_submission_comment,
    generate_wrong_course_comment,
    get_file_changes_summary,
    find_duplicate_submission,
    normalize_issue_title,
)
from .rag_agent import FAQDecision


# Only recognized field headings act as delimiters; other Markdown headings in
# the question or answer body remain content (see issue #169).
_HEADER_RE = re.compile(r'#{1,6}\s+(Course|Question|Answer|Checklist)\b', re.IGNORECASE)


def parse_full_issue_body(issue_body: str) -> tuple[str, str, str]:
    """
    Parse a structured GitHub issue body into (course, question, answer).

    Expected sections use Markdown headings at any level: `## Course`,
    `## Question`, and `## Answer` (a trailing `## Checklist` is ignored).
    Raises ValueError if any of the three is missing or empty.
    """
    sections: dict[str, list[str]] = {}
    current = None

    for line in issue_body.strip().splitlines():
        header = _HEADER_RE.match(line.strip())
        if header:
            current = header.group(1).lower()
            sections.setdefault(current, [])
        elif current:
            sections[current].append(line.strip())

    parsed = {}
    for name, lines in sections.items():
        parsed[name] = '\n'.join(lines).strip()

    course = parsed.get('course')
    question = parsed.get('question')
    answer = parsed.get('answer')

    if not course or not question or not answer:
        raise ValueError("Could not parse course, question and answer from issue body")

    return course, question, answer


def build_issue_ref(issue_number: int, course: str | None = None) -> dict:
    """
    Build the {issue_number, issue_url, course} dict for trace input.

    Repo comes from GITHUB_REPOSITORY (owner/repo), defaulting to
    DataTalksClub/faq for local runs.
    """
    repo = os.environ.get("GITHUB_REPOSITORY", "DataTalksClub/faq")
    return {
        "issue_number": issue_number,
        "issue_url": f"https://github.com/{repo}/issues/{issue_number}",
        "course": course,
    }


def validate_faq_decision(
    decision: FAQDecision,
    course_dir: Path,
    doc_index: dict,
) -> None:
    """Reject incomplete or internally inconsistent model output before writing."""
    decision.question = normalize_issue_title(decision.question)
    metadata = read_metadata(course_dir)
    section_ids = {section["id"] for section in metadata["sections"]}

    if decision.action in ("NEW", "UPDATE"):
        if not decision.proposed_content or not decision.proposed_content.strip():
            raise ValueError(f"{decision.action} decision requires a non-empty answer")
        if decision.section_id not in section_ids:
            raise ValueError(f"Unknown FAQ section: {decision.section_id!r}")
        if decision.order < -1:
            raise ValueError(f"Invalid FAQ sort order: {decision.order}")

    if decision.action in ("UPDATE", "DUPLICATE"):
        if decision.document_id not in doc_index:
            raise ValueError(
                f"{decision.action} decision references unknown FAQ document "
                f"{decision.document_id!r}"
            )

    if decision.action == "DUPLICATE":
        # The referenced file is the source of truth for the link in the close
        # comment; do not trust a possibly inconsistent model section.
        decision.section_id = doc_index[decision.document_id].parent.name


def build_invalid_proposal_decision(issue_number: int) -> dict:
    """Create a clear close response for an empty or unstructured proposal."""
    return {
        "action": "INVALID_PROPOSAL",
        "issue_number": issue_number,
        "comment": (
            "This FAQ proposal is missing a course, question, or answer, so I’m "
            "closing it for now. Please edit the issue to include all three "
            "sections from the FAQ proposal form, then reopen it for review."
        ),
    }


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description='Process FAQ proposal from GitHub issue')
    parser.add_argument('--issue-body', required=True, help='GitHub issue body text')
    parser.add_argument('--issue-title', default='', help='Current GitHub issue title')
    parser.add_argument('--issue-number', type=int, required=True, help='GitHub issue number')
    parser.add_argument('--model', default=DEFAULT_MODEL, help='OpenAI model to use')
    parser.add_argument('--output-dir', default='.', help='Output directory for results')
    parser.add_argument(
        '--related-issues-file',
        help='Optional JSON list of open issues used to catch exact duplicate FAQ proposals',
    )

    args = parser.parse_args()

    try:
        # Parse issue body (extracts course, question, and answer)
        print("Parsing issue body...")
        try:
            course, question, answer = parse_full_issue_body(args.issue_body)
        except ValueError:
            output = build_invalid_proposal_decision(args.issue_number)
            output_file = Path(args.output_dir) / 'faq_decision.json'
            output_file.write_text(json.dumps(output, indent=2), encoding='utf-8')
            print(f"Incomplete proposal; output written to: {output_file}")
            return

        course = normalize_course_id(course)

        print(f"Course: {course}")
        print(f"Question: {question[:100]}...")
        print(f"Answer: {answer[:100]}...")

        # Get OpenAI API key from environment only after deterministic input checks.
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        if not openai_api_key:
            print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
            sys.exit(1)

        # Set up paths
        questions_dir = Path(os.environ.get('QUESTIONS_DIR', '_questions'))
        course_dir = questions_dir / course
        if not course_dir.exists():
            print(f"Error: Course directory {course_dir} does not exist", file=sys.stderr)
            sys.exit(1)

        related_issues = []
        if args.related_issues_file:
            related_issues = json.loads(
                Path(args.related_issues_file).read_text(encoding='utf-8')
            )
        duplicate_issue = find_duplicate_submission(
            question,
            course,
            args.issue_number,
            related_issues,
            issue_title=args.issue_title,
        )
        if duplicate_issue:
            output = {
                'action': 'DUPLICATE_SUBMISSION',
                'issue_number': args.issue_number,
                'issue_title': normalize_issue_title(question),
                'course': course,
                'duplicate_issue_number': duplicate_issue['number'],
                'comment': generate_duplicate_submission_comment(duplicate_issue),
            }
            output_file = Path(args.output_dir) / 'faq_decision.json'
            output_file.write_text(json.dumps(output, indent=2), encoding='utf-8')
            print(f"Duplicate proposal found in issue #{duplicate_issue['number']}")
            print(f"Output written to: {output_file}")
            return

        # Issue ref lands in the triage trace input via @track.
        issue_ref = build_issue_ref(args.issue_number, course)

        # Process proposal
        print("\nProcessing FAQ proposal with LLM...")
        faq_decision = process_faq_proposal(
            course_dir=course_dir,
            question=question,
            answer=answer,
            openai_api_key=openai_api_key,
            model=args.model,
            issue_ref=issue_ref,
        )

        doc_index = find_question_files(course_dir)
        validate_faq_decision(faq_decision, course_dir, doc_index)

        print(f"\nDecision: {faq_decision.action}")
        print(f"Rationale: {faq_decision.rationale}")
        print(f"Section: {faq_decision.section_id}")

        # Prepare output
        output = {
            'action': faq_decision.action,
            'decision': faq_decision.model_dump(),
            'issue_number': args.issue_number,
            'issue_title': normalize_issue_title(
                faq_decision.question if faq_decision.action in ('NEW', 'UPDATE')
                else question
            ),
            'course': course,
        }

        # Handle different actions
        if faq_decision.action in ('NEW', 'UPDATE'):
            print(f"\nApplying {faq_decision.action} to FAQ file...")
            if faq_decision.action == 'NEW':
                file_path = create_new_faq_file(course_dir, doc_index, faq_decision)
            else:
                file_path = update_existing_faq_file(course_dir, doc_index, faq_decision)

            output['file_path'] = str(file_path)
            actual_sort_order = int(file_path.name.split('_', maxsplit=1)[0])
            output['pr_body'] = generate_pr_body(
                faq_decision,
                args.issue_number,
                course,
                actual_sort_order=actual_sort_order,
            )
            output['changes'] = get_file_changes_summary(faq_decision.action, file_path, course_dir)

            print(f"{faq_decision.action}: {file_path}")

        elif faq_decision.action == 'DUPLICATE':
            print("\nGenerating duplicate comment...")
            output['comment'] = generate_duplicate_comment(
                faq_decision,
                course,
                site_url='https://datatalks.club/faq'  # Update with actual URL
            )

        elif faq_decision.action == 'WRONG_COURSE':
            print("\nGenerating wrong course comment...")
            output['comment'] = generate_wrong_course_comment(faq_decision, course)

        # Write output as JSON for GitHub Actions
        output_file = Path(args.output_dir) / 'faq_decision.json'
        with open(output_file, 'w') as f:
            json.dump(output, f, indent=2)

        print(f"\nOutput written to: {output_file}")
        print("\nDone!")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
