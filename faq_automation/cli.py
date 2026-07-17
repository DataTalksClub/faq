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
from .core import find_question_files
from .actions import (
    create_new_faq_file,
    update_existing_faq_file,
    generate_pr_body,
    generate_duplicate_comment,
    generate_wrong_course_comment,
    get_file_changes_summary,
)


# Only these template headers act as delimiters; a "### ..." line inside the
# question or answer body is kept as content (see issue #169).
_HEADER_RE = re.compile(r'###\s+(Course|Question|Answer|Checklist)\b', re.IGNORECASE)


def parse_full_issue_body(issue_body: str) -> tuple[str, str, str]:
    """
    Parse a structured GitHub issue body into (course, question, answer).

    Expected sections: `### Course`, `### Question`, `### Answer` (a trailing
    `### Checklist` is ignored). Raises ValueError if any of the three is
    missing or empty.
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


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description='Process FAQ proposal from GitHub issue')
    parser.add_argument('--issue-body', required=True, help='GitHub issue body text')
    parser.add_argument('--issue-number', type=int, required=True, help='GitHub issue number')
    parser.add_argument('--model', default=DEFAULT_MODEL, help='OpenAI model to use')
    parser.add_argument('--output-dir', default='.', help='Output directory for results')

    args = parser.parse_args()

    # Get OpenAI API key from environment
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    if not openai_api_key:
        print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    try:
        # Parse issue body (extracts course, question, and answer)
        print("Parsing issue body...")
        course, question, answer = parse_full_issue_body(args.issue_body)
        print(f"Course: {course}")
        print(f"Question: {question[:100]}...")
        print(f"Answer: {answer[:100]}...")

        # Set up paths
        questions_dir = Path(os.environ.get('QUESTIONS_DIR', '_questions'))
        course_dir = questions_dir / course
        if not course_dir.exists():
            print(f"Error: Course directory {course_dir} does not exist", file=sys.stderr)
            sys.exit(1)

        # Process proposal
        print("\nProcessing FAQ proposal with LLM...")
        faq_decision = process_faq_proposal(
            course_dir=course_dir,
            question=question,
            answer=answer,
            openai_api_key=openai_api_key,
            model=args.model
        )

        print(f"\nDecision: {faq_decision.action}")
        print(f"Rationale: {faq_decision.rationale}")
        print(f"Section: {faq_decision.section_id}")

        # Prepare output
        output = {
            'action': faq_decision.action,
            'decision': faq_decision.model_dump(),
            'issue_number': args.issue_number,
            'course': course,
        }

        # Handle different actions
        if faq_decision.action in ('NEW', 'UPDATE'):
            print(f"\nApplying {faq_decision.action} to FAQ file...")
            doc_index = find_question_files(course_dir)
            if faq_decision.action == 'NEW':
                file_path = create_new_faq_file(course_dir, doc_index, faq_decision)
            else:
                file_path = update_existing_faq_file(course_dir, doc_index, faq_decision)

            output['file_path'] = str(file_path)
            output['pr_body'] = generate_pr_body(faq_decision, args.issue_number, course)
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
