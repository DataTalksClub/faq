"""
Unit tests for the WRONG_COURSE decision path and the eval Batch API plumbing.
"""

import json

from faq_automation.core import read_course_catalog
from faq_automation.rag_agent import FAQDecision
from faq_automation.actions import generate_wrong_course_comment
from faq_automation.evals import batch


def make_decision(**overrides):
    """Build a WRONG_COURSE decision, overriding fields per test."""
    fields = {
        'action': 'WRONG_COURSE',
        'rationale': 'This is about RAG monitoring, which the LLM course covers.',
        'document_id': '',
        'section_rationale': 'No section in this course covers RAG.',
        'section_id': '',
        'order': -1,
        'question': 'How do I adapt RAGWithMetrics for OpenAI-compatible endpoints?',
        'suggested_course': 'llm-zoomcamp',
    }
    fields.update(overrides)
    return FAQDecision(**fields)


class TestReadCourseCatalog:
    """Test building the course catalog the agent uses to name the right course."""

    def _write_course(self, questions_dir, course_id, course_name):
        course_dir = questions_dir / course_id
        course_dir.mkdir()
        metadata = f'course: {course_id}\ncourse_name: "{course_name}"\nsections: []\n'
        (course_dir / '_metadata.yaml').write_text(metadata)

    def test_lists_every_course(self, tmp_path):
        self._write_course(tmp_path, 'llm-zoomcamp', 'LLM Zoomcamp')
        self._write_course(tmp_path, 'mlops-zoomcamp', 'MLOps Zoomcamp')

        catalog = read_course_catalog(tmp_path)

        assert catalog == [
            {'course': 'llm-zoomcamp', 'course_name': 'LLM Zoomcamp'},
            {'course': 'mlops-zoomcamp', 'course_name': 'MLOps Zoomcamp'},
        ]

    def test_ignores_directories_without_metadata(self, tmp_path):
        self._write_course(tmp_path, 'llm-zoomcamp', 'LLM Zoomcamp')
        (tmp_path / '_drafts').mkdir()

        catalog = read_course_catalog(tmp_path)

        assert len(catalog) == 1
        assert catalog[0]['course'] == 'llm-zoomcamp'


class TestWrongCourseComment:
    """Test the comment posted before the bot closes a misfiled issue."""

    def test_names_the_suggested_course(self):
        comment = generate_wrong_course_comment(make_decision(), 'machine-learning-zoomcamp')

        assert 'machine-learning-zoomcamp' in comment
        assert 'llm-zoomcamp' in comment
        assert 'This is about RAG monitoring' in comment

    def test_without_suggested_course_still_asks_to_refile(self):
        comment = generate_wrong_course_comment(
            make_decision(suggested_course=None),
            'machine-learning-zoomcamp',
        )

        assert 'pick the right course' in comment
        assert 'None' not in comment


class TestBatchRequests:
    """Test the JSONL request the eval runner sends to the Batch API."""

    def test_build_request_targets_the_responses_endpoint(self):
        messages = [{'role': 'user', 'content': 'hello'}]

        request = batch.build_request('case-0-issue-311', messages, 'gpt-5-nano')

        assert request['custom_id'] == 'case-0-issue-311'
        assert request['method'] == 'POST'
        assert request['url'] == '/v1/responses'
        assert request['body']['model'] == 'gpt-5-nano'
        assert request['body']['input'] == messages
        assert request['body']['text']['format']['strict'] is True

    def test_build_request_is_json_serializable(self):
        request = batch.build_request('case-0', [{'role': 'user', 'content': 'hi'}], 'gpt-5-nano')

        assert json.loads(json.dumps(request)) == request

    def test_parse_decision_reads_structured_output(self):
        decision = make_decision()
        body = {
            'output': [
                {'type': 'reasoning', 'content': []},
                {
                    'type': 'message',
                    'content': [{'type': 'output_text', 'text': decision.model_dump_json()}],
                },
            ]
        }

        parsed = batch.parse_decision(body)

        assert parsed.action == 'WRONG_COURSE'
        assert parsed.suggested_course == 'llm-zoomcamp'
