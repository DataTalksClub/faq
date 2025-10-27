"""
RAG Agent for FAQ Triage

Uses LLM and retrieval to decide how to handle new FAQ proposals.
"""

import json
from typing import List, Optional, Literal
from pathlib import Path

from pydantic import BaseModel, Field
from openai import OpenAI
from minsearch import Index

from .core import read_questions, read_metadata, keep_relevant


# Prompt templates
PROMPT_TEMPLATE = """
<ENTRY>
{entry}
</ENTRY>
<SEARCH_RESULTS>
{results}
</SEARCH_RESULTS>
<SECTIONS>
{sections}
</SECTIONS>
""".strip()

SYSTEM_PROMPT = """
You are an assistant that helps maintain a student FAQ repository.

Given:
1. A new proposal in ENTRY
2. A set of top similar existing FAQs in SEARCH_RESULTS

You must decide one of:
- `NEW`: create a new FAQ file
- `UPDATE:<document_id>`: the proposal adds meaningful info to an existing FAQ
- `DUPLICATE:<document_id>`: the proposal is already fully covered, no need to update or add

Rules
- NEW if the question is not covered in FAQ
- UPDATE if the existing FAQ is about the same issue but missing context or details
- DUPLICATE if the existing FAQ already answers the question fully
- Do not invent unrelated content, base decisions strictly on the provided proposal and FAQ excerpts
- When UPDATE, merge old and new answers into one, making the updated answer complete and containing all the information from both
- When UPDATE, make sure the new question is reflective of the both new and old records
- Carefully analyse existing sections to decide where it goes. Generic questions that don't fit any other section should go to "general"

Example reasoning
- If two FAQs are semantically the same but wording differs slightly → DUPLICATE.
- If an FAQ exists but lacks troubleshooting steps the student provided → UPDATE.
- If the topic is not covered in existing FAQs → NEW.
""".strip()


class FAQDecision(BaseModel):
    """
    Unified decision object returned by your triage agent.
    Contains placement (module/order/title) and action-specific payload.
    """

    # What to do
    action: Literal["NEW", "UPDATE", "DUPLICATE"] = Field(
        ...,
        description=(
            "Decision:\n"
            "- NEW: create a new FAQ file.\n"
            "- UPDATE: merge the proposal into an existing FAQ.\n"
            "- DUPLICATE: proposal is already covered by an existing FAQ."
        ),
    )
    rationale: str = Field(..., description="1-2 sentences explaining the decision.")
    document_id: str = Field(
        ...,
        description=(
            "ID to act on:\n"
            "- NEW → document_id to use for the new file.\n"
            "- UPDATE/DUPLICATE → document_id of the existing FAQ."
        ),
    )

    section_rationale: str = Field(..., description="1-2 sentences explaining why this section was chosen")
    section_id: str = Field(..., description="Section for this FAQ (e.g 'module-1').")

    order: int = Field(..., description="Integer controlling sort order within the module. Set to number if it should be placed near existing FAQ records, set to -1 it it should go at the end of the section")

    question: str = Field(..., description="FAQ question title displayed to users (plain-text question).")

    # Action-specific payload
    proposed_content: Optional[str] = Field(
        None,
        description="Only for NEW and UPDATE: markdown file with the answer. The question is not included. No headers.",
    )

    filename_slug: Optional[str] = Field(
        None,
        description="Only for NEW: file-system friendly slug with hyphens, up to 50 characters",
    )

    # Notes
    warnings: List[str] = Field(
        default_factory=list,
        description="Optional warnings (e.g., sort order collision, module mismatch).",
    )


class FAQAgent:
    """Agent for processing FAQ proposals using RAG and LLM"""

    def __init__(self, course_dir: Path, openai_api_key: str, model: str = "gpt-5-nano"):
        """
        Initialize the FAQ Agent

        Args:
            course_dir: Path to the course directory (e.g., _questions/machine-learning-zoomcamp)
            openai_api_key: OpenAI API key
            model: OpenAI model to use (default: gpt-4)
        """
        self.course_dir = course_dir
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.model = model

        # Load existing FAQs and metadata
        self.documents = read_questions(course_dir)
        self.metadata = read_metadata(course_dir)

        # Build search index
        self.index = Index(
            text_fields=['section', 'question', 'answer'],
            keyword_fields=['course', 'section_id'],
        )
        self.index.fit(self.documents)

    def process_proposal(self, question: str, answer: str, num_results: int = 5) -> FAQDecision:
        """
        Process a new FAQ proposal

        Args:
            question: The proposed question
            answer: The proposed answer
            num_results: Number of similar FAQs to retrieve (default: 5)

        Returns:
            FAQDecision object with action and all necessary information
        """
        # Search for similar existing FAQs
        proposal = f"## {question}\n\n{answer}"
        results = self.index.search(proposal, num_results=num_results)
        results = keep_relevant(results)

        # Build prompt
        prompt = PROMPT_TEMPLATE.format(
            entry=proposal,
            results=json.dumps(results),
            sections=json.dumps(self.metadata['sections'])
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        # Call OpenAI with structured output
        response = self.openai_client.responses.parse(
            model=self.model,
            input=messages,
            text_format=FAQDecision,
        )

        message = next(filter(lambda o: o.type == 'message', response.output))
        faq_decision = message.content[0].parsed

        return faq_decision


def process_faq_proposal(
    course_dir: Path,
    question: str,
    answer: str,
    openai_api_key: str,
    model: str = "gpt-5-nano"
) -> FAQDecision:
    """
    Convenience function to process a single FAQ proposal

    Args:
        course_dir: Path to the course directory
        question: The proposed question
        answer: The proposed answer
        openai_api_key: OpenAI API key
        model: OpenAI model to use (default: gpt-4)

    Returns:
        FAQDecision object
    """
    agent = FAQAgent(course_dir, openai_api_key, model)
    return agent.process_proposal(question, answer)
