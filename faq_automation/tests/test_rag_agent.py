import json
import pytest

from faq_automation.rag_agent import (
    FAQAgent,
    FAQDecision,
    SYSTEM_PROMPT,
    enforce_homework_assignment,
    filter_other_homework_results,
)


def make_decision(
    *, action="UPDATE", document_id="hw4-doc", section_id="module-4-homework",
    question="Why are my results different?", proposed_content="Check the assignment settings.",
):
    return FAQDecision(
        action=action,
        rationale="The proposal matches a result mismatch FAQ.",
        document_id=document_id,
        section_rationale="This homework section looks related.",
        section_id=section_id,
        order=4,
        question=question,
        proposed_content=proposed_content,
        filename_slug="results-differ",
    )


def test_filter_other_homework_results_keeps_same_assignment_and_non_homework_faqs():
    results = [
        {"section_id": "module-2-homework", "question": "Different answers"},
        {"section_id": "module-6-homework", "question": "Homework 6 question"},
        {"section_id": "module-3", "question": "DictVectorizer"},
    ]

    filtered = filter_other_homework_results(results, 6)

    assert filtered == results[1:]


def test_prompt_requires_full_coverage_before_duplicate_and_preserves_update_details():
    assert "DUPLICATE` only when an existing FAQ already covers the same problem" in SYSTEM_PROMPT
    assert "all useful, supported information in ENTRY" in SYSTEM_PROMPT
    assert "include the material new details from ENTRY" in SYSTEM_PROMPT
    assert "Choose `NEW` only when no retrieved FAQ covers the same underlying problem" in SYSTEM_PROMPT


def test_build_messages_excludes_other_numbered_homeworks_from_retrieval():
    class FakeIndex:
        def search(self, query, num_results):
            return [
                {"document_id": "hw2", "section_id": "module-2-homework", "question": "Answer mismatch", "answer": "Homework 2"},
                {"document_id": "hw4", "section_id": "module-4-homework", "question": "Accuracy mismatch", "answer": "Homework 4"},
                {"document_id": "hw6", "section_id": "module-6-homework", "question": "RMSE mismatch", "answer": "Homework 6"},
                {"document_id": "lesson", "section_id": "module-3", "question": "DictVectorizer", "answer": "Fit on training data"},
            ]

    agent = FAQAgent.__new__(FAQAgent)
    agent.index = FakeIndex()
    agent.metadata = {
        "course": "machine-learning-zoomcamp",
        "course_name": "Machine Learning Zoomcamp",
        "sections": [{"id": "module-6-homework"}],
    }
    agent.catalog = []

    messages = agent.build_messages(
        "Why is my Homework 6 Question 2 RMSE different?",
        "I followed the assignment but got another value.",
    )
    user_prompt = messages[1]["content"]
    start = user_prompt.index("<SEARCH_RESULTS>") + len("<SEARCH_RESULTS>")
    end = user_prompt.index("</SEARCH_RESULTS>")
    results = json.loads(user_prompt[start:end].strip())

    assert {result["document_id"] for result in results} == {"hw6", "lesson"}


def test_cross_homework_update_becomes_new_in_matching_section():
    question = "Why is my Homework 6 Question 2 RMSE different?"
    decision = make_decision()
    sections = [{"id": "module-6-homework"}]
    documents = [{"document_id": "hw4-doc", "section_id": "module-4-homework"}]

    corrected = enforce_homework_assignment(decision, question, sections, documents)

    assert corrected.action == "NEW"
    assert corrected.document_id == ""
    assert corrected.question == question
    assert corrected.section_id == "module-6-homework"
    assert corrected.order == -1
    assert corrected.proposed_content == decision.proposed_content
    assert corrected.warnings


def test_new_homework_proposal_is_routed_to_its_matching_section():
    question = "How do I solve Homework 6 Question 2?"
    decision = make_decision(action="NEW", document_id="new-doc")

    corrected = enforce_homework_assignment(
        decision,
        question,
        [{"id": "module-6-homework"}],
        [],
    )

    assert corrected.action == "NEW"
    assert corrected.section_id == "module-6-homework"
    assert corrected.question == question
    assert corrected.order == -1


def test_cross_homework_duplicate_is_not_closed():
    question = "How do I solve Homework 6 Question 2?"
    decision = make_decision(
        action="DUPLICATE",
        proposed_content=None,
    )

    with pytest.raises(ValueError, match="Refusing to close Homework 6"):
        enforce_homework_assignment(
            decision,
            question,
            [{"id": "module-6-homework"}],
            [{"document_id": "hw4-doc", "section_id": "module-4-homework"}],
        )


def test_same_homework_update_is_unchanged():
    decision = make_decision(document_id="hw6-doc", section_id="module-6-homework")

    corrected = enforce_homework_assignment(
        decision,
        "Why is my Homework 6 Question 2 RMSE different?",
        [{"id": "module-6-homework"}],
        [{"document_id": "hw6-doc", "section_id": "module-6-homework"}],
    )

    assert corrected is decision
