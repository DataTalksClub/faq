"""
RAG Agent for FAQ Triage

Uses LLM and retrieval to decide how to handle new FAQ proposals.
"""

import os
import json
from typing import List, Optional, Literal
from pathlib import Path

from pydantic import BaseModel, Field
from openai import OpenAI
from openai.lib._pydantic import to_strict_json_schema
from minsearch import Index

from .core import (
    keep_relevant,
    read_course_catalog,
    read_metadata,
    read_questions,
    reciprocal_rank_fusion,
)


# Single source of truth for the model used by both automation and evals.
# Override per-run with the FAQ_MODEL environment variable.
# See docs/model-choice.md for why this model and what it trades away.
DEFAULT_MODEL = os.environ.get("FAQ_MODEL", "gpt-5.4-nano")


# Prompt templates
PROMPT_TEMPLATE = """
<COURSE>
{course}
</COURSE>
<COURSE_CATALOG>
{catalog}
</COURSE_CATALOG>
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
1. The course the proposal was filed against in COURSE
2. Every course in the FAQ repository in COURSE_CATALOG
3. A new proposal in ENTRY
4. A set of top similar existing FAQs in SEARCH_RESULTS
5. The full list of sections with comments in SECTIONS

SEARCH_RESULTS and SECTIONS describe COURSE only — they never contain entries
or sections from the other courses in COURSE_CATALOG.

You must decide one of:
- `NEW`: create a new FAQ file
- `UPDATE:<document_id>`: the proposal adds meaningful info to an existing FAQ
- `DUPLICATE:<document_id>`: the proposal is already fully covered, no need to update or add
- `WRONG_COURSE`: the proposal is about a different course and cannot be filed here at all

## Step 1: does this proposal belong to COURSE at all?
Answer this before anything else. Students pick the course from a dropdown when filing
and sometimes pick the wrong one, so ENTRY is not guaranteed to be about COURSE.

Ask: which course in COURSE_CATALOG owns the tools, datasets, and modules this ENTRY
talks about? If that course is COURSE, continue to step 2. If it is plainly a different
course, the answer is WRONG_COURSE — set suggested_course to that course's id and stop.
The strict conditions in "Wrong course rules" below decide what counts as plainly.

## Step 2: action rules
Only once the proposal belongs to COURSE:
- NEW if the question is not covered in FAQ
- UPDATE if the existing FAQ is about the same issue but missing context or details
- DUPLICATE if the existing FAQ already answers the question fully
- Do not invent unrelated content, base decisions strictly on the provided proposal and FAQ excerpts
- When UPDATE, merge old and new answers into one, making the updated answer complete and containing all the information from both
- When UPDATE, make sure the new question is reflective of the both new and old records
- Do NOT create a NEW entry for questions that are transient/specific to a particular cohort (e.g. "why does this dataset have 1350 rows instead of 1208" — the FAQ is a living document, counts change). Mark these as DUPLICATE.

## Wrong course rules
Students pick the course from a dropdown when filing the proposal, and occasionally pick
the wrong one. WRONG_COURSE catches only that mistake — it is not a rejection mechanism.

- Choose WRONG_COURSE only when BOTH hold:
  1. The proposal is clearly about material owned by a different course in COURSE_CATALOG.
  2. No module or topic section in SECTIONS covers it.
- Catch-all sections ("general", "misc", "Miscellaneous") do not satisfy condition 2.
  They exist for stray questions from THIS course's students, not as a home for another
  course's material. Reaching for one because nothing else fits is the signal to check
  the course, not a placement. Decide as if those sections did not exist.
- Require positive evidence of the other course: the entry names that course's specific
  tools, datasets, modules, or code. Examples: the NYC taxi dataset, Kestra, dbt, BigQuery,
  Spark, Kafka, or Terraform point to data-engineering-zoomcamp; RAG, embeddings, vector
  search, Qdrant, or LLM evaluation point to llm-zoomcamp; MLflow, model registries, or
  Prefect point to mlops-zoomcamp.
- Courses share tools. Kestra appears in both the DE and LLM courses; Docker appears in
  almost all of them. The SECTIONS comments decide who owns a topic — if a section covers
  it, this is the right course, no matter which other course also uses that tool.
- Never choose WRONG_COURSE for course-agnostic tooling (Python, Docker, git, uv, conda,
  pip, VS Code, WSL, Codespaces, Jupyter) unless it is tied to another course's material.
- A topic missing from SEARCH_RESULTS or fitting no section neatly is NEW, not WRONG_COURSE.
  Absence of coverage is never evidence of the wrong course.
- When unsure, prefer NEW, UPDATE, or DUPLICATE. A misfiled entry a human can move is a far
  cheaper mistake than rejecting a valid proposal.
- For WRONG_COURSE: set suggested_course to the course id from COURSE_CATALOG that owns the
  topic, leave proposed_content empty, set section_id to "" and order to -1.

## Section placement rules
- Decide the section based on the proposal content and the SECTIONS metadata. Use the "comment" field.
- Give the SECTIONS `comment` field more weight than SEARCH_RESULTS when choosing a section.
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
    action: Literal["NEW", "UPDATE", "DUPLICATE", "WRONG_COURSE"] = Field(
        ...,
        description=(
            "Decision:\n"
            "- NEW: create a new FAQ file.\n"
            "- UPDATE: merge the proposal into an existing FAQ.\n"
            "- DUPLICATE: proposal is already covered by an existing FAQ.\n"
            "- WRONG_COURSE: proposal belongs to a different course entirely."
        ),
    )
    rationale: str = Field(..., description="1-2 sentences explaining the decision.")
    document_id: str = Field(
        ...,
        description=(
            "ID to act on:\n"
            "- NEW → document_id to use for the new file.\n"
            "- UPDATE/DUPLICATE → document_id of the existing FAQ.\n"
            "- WRONG_COURSE → empty string."
        ),
    )

    section_rationale: str = Field(..., description="1-2 sentences explaining why this section was chosen")
    section_id: str = Field(..., description="Section for this FAQ (e.g 'module-1'). Empty string for WRONG_COURSE.")

    suggested_course: Optional[str] = Field(
        None,
        description="Only for WRONG_COURSE: the course id from COURSE_CATALOG that the proposal actually belongs to.",
    )

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


# `responses.parse` derives this from FAQDecision on its own. The Batch API takes
# raw JSON bodies instead, so callers that build their own request need it spelled out.
RESPONSE_TEXT_FORMAT = {
    "type": "json_schema",
    "name": "FAQDecision",
    "schema": to_strict_json_schema(FAQDecision),
    "strict": True,
}


def extract_decision(response) -> FAQDecision:
    """Pull the parsed FAQDecision out of a Responses API result."""
    message = next(filter(lambda o: o.type == 'message', response.output))
    return message.content[0].parsed


class FAQAgent:
    """Agent for processing FAQ proposals using RAG and LLM"""

    def __init__(
        self,
        course_dir: Path,
        openai_api_key: str,
        model: str = DEFAULT_MODEL,
        questions_dir: Optional[Path] = None,
    ):
        """
        Initialize the FAQ Agent

        Args:
            course_dir: Path to the course directory (e.g., _questions/machine-learning-zoomcamp)
            openai_api_key: OpenAI API key
            model: OpenAI model to use (default: DEFAULT_MODEL)
            questions_dir: Directory holding all courses, used to build the course
                catalog for WRONG_COURSE decisions. Defaults to course_dir's parent.
                Pass explicitly when course_dir is a copy outside the repository.
        """
        self.course_dir = course_dir
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.model = model

        if questions_dir is None:
            questions_dir = course_dir.parent

        # Load existing FAQs and metadata
        self.documents = read_questions(course_dir)
        self.metadata = read_metadata(course_dir)
        self.catalog = read_course_catalog(questions_dir)

        # Build search index
        self.index = Index(
            text_fields=['question', 'answer'],
            keyword_fields=['course', 'section_id'],
        )
        self.index.fit(self.documents)

    def build_messages(self, question: str, answer: str, num_results: int = 5) -> List[dict]:
        """
        Build the model input for a proposal: retrieval plus prompt assembly.

        Split out from process_proposal so the eval Batch API runner can build
        the exact same request without calling the live endpoint.

        Args:
            question: The proposed question
            answer: The proposed answer
            num_results: Number of similar FAQs to retrieve (default: 5)

        Returns:
            List of chat messages ready to send to the Responses API
        """
        # Search the question separately so a vague or noisy proposed answer
        # cannot bury an otherwise strong question match. Keep the existing
        # full-proposal search as the stronger signal.
        proposal = f"## {question}\n\n{answer}"
        candidate_count = max(num_results * 2, 10)
        question_results = self.index.search(
            question,
            num_results=candidate_count,
        )
        proposal_results = self.index.search(
            proposal,
            num_results=candidate_count,
        )
        results = reciprocal_rank_fusion(
            [question_results, proposal_results],
            weights=[1.0, 2.0],
            limit=num_results,
        )
        results = keep_relevant(results)

        # Build prompt
        prompt = PROMPT_TEMPLATE.format(
            course=json.dumps({
                'course': self.metadata['course'],
                'course_name': self.metadata['course_name'],
            }),
            catalog=json.dumps(self.catalog),
            entry=proposal,
            results=json.dumps(results),
            sections=json.dumps(self.metadata['sections'])
        )

        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

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
        messages = self.build_messages(question, answer, num_results)

        # Call OpenAI with structured output
        response = self.openai_client.responses.parse(
            model=self.model,
            input=messages,
            text_format=FAQDecision,
        )

        return extract_decision(response)


def process_faq_proposal(
    course_dir: Path,
    question: str,
    answer: str,
    openai_api_key: str,
    model: str = DEFAULT_MODEL
) -> FAQDecision:
    """
    Convenience function to process a single FAQ proposal

    Args:
        course_dir: Path to the course directory
        question: The proposed question
        answer: The proposed answer
        openai_api_key: OpenAI API key
        model: OpenAI model to use (default: DEFAULT_MODEL)

    Returns:
        FAQDecision object
    """
    agent = FAQAgent(course_dir, openai_api_key, model)
    return agent.process_proposal(question, answer)
