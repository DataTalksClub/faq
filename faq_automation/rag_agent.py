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
3. The full list of sections with comments in SECTIONS

You must decide one of:
- `NEW`: create a new FAQ file
- `UPDATE:<document_id>`: the proposal adds meaningful info to an existing FAQ
- `DUPLICATE:<document_id>`: the proposal is already fully covered, no need to update or add

## Action rules
- NEW if the question is not covered in FAQ
- UPDATE if the existing FAQ is about the same issue but missing context or details
- DUPLICATE if the existing FAQ already answers the question fully
- Do not invent unrelated content, base decisions strictly on the provided proposal and FAQ excerpts
- When UPDATE, merge old and new answers into one, making the updated answer complete and containing all the information from both
- When UPDATE, make sure the new question is reflective of the both new and old records
- Do NOT create a NEW entry for questions that are transient/specific to a particular cohort (e.g. "why does this dataset have 1350 rows instead of 1208" — the FAQ is a living document, counts change). Mark these as DUPLICATE.

## Section placement rules
- Decide the section based on the proposal content and the SECTIONS metadata (especially the "comment" field), NOT based on where the SEARCH_RESULTS happen to come from. The search results are for duplicate detection, not section guidance — they may come from the wrong section due to keyword overlap.
- Read the "comment" field of each section in SECTIONS carefully. It describes exactly what topics belong there.
- Match the proposal to the section whose comment covers the same tools, topics, or module.
- NEVER default to "general" for a technical question. "general" is only for course logistics (schedule, certificate, deadlines, leaderboard, project rules).
- Tool-to-section mapping (use the comment field to confirm):
  - dlt questions → workshop section (e.g. "workshop-1-dlthub" or "workshops-dlthub"), NOT module-3 or general. dlt is NOT dbt.
  - Bruin questions → the module about data platforms (e.g. "module-5" with comment mentioning Bruin)
  - DuckDB questions → the module about dbt/analytics engineering (DuckDB is used with dbt)
  - Docker questions → the module or section specifically about Docker
  - Kestra/orchestration questions → the module about workflow orchestration
  - Homework-specific questions → the dedicated homework section (e.g. "module-2-homework"), NOT the main module section
- Set the order to place the FAQ near related entries (e.g. if it logically follows FAQ #5, use order 6). Use -1 only to append to the end. The system handles sort order collisions automatically — never worry about picking an existing number.

## Example reasoning
- If two FAQs are semantically the same but wording differs slightly -> DUPLICATE.
- If an FAQ exists but lacks troubleshooting steps the student provided -> UPDATE.
- If the topic is not covered in existing FAQs -> NEW.

## Content quality rules
- Start with a direct answer. Do NOT use markdown headers (no #, ##, ### lines) to structure the answer — write flowing prose with bullet points where appropriate.
- Do NOT use bold-only lines as section headers (e.g. **Step 1:** on its own line). Weave steps into prose or use a numbered list.
- Keep answers concise (under 40 lines). Do not pad with generic advice.
- If you include Python code:
  - Every variable, class, and function referenced in the code MUST be defined or imported in the same code block or a preceding one.
  - For example, if you write `response_format=Questions`, you MUST show the Pydantic model definition for `Questions`.
  - For example, if you pass `messages=some_var`, you MUST define `some_var` before using it.
  - Code must be runnable as-is by a student copy-pasting it.

## Code formatting rules
- Wrap all code identifiers (variables, classes, functions, method names, parameters, module names, etc.) in backticks.
- Use fenced code blocks (triple backticks) for multi-line snippets. Always specify the language.
- Use 4 spaces for indentation inside code blocks.
- Preserve the original meaning of technical text; only adjust for clarity and formatting.
"""


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

    order: int = Field(..., description="Integer controlling sort order within the section. Set to the position where the FAQ logically belongs (near related entries). Set to -1 to append to end. The system handles collisions automatically.")

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
