"""Unit tests for Slack fetch helpers."""

import json

from faq_automation.slack_fetch import (
    SlackMessage,
    build_parser,
    resolve_course_channel,
    should_skip_slack_message,
    slack_ts_to_iso,
    write_outputs,
)


def test_parser_defaults_to_llm_zoomcamp():
    parser = build_parser()
    args = parser.parse_args([])

    assert args.course == "llm-zoomcamp"
    assert args.channel is None
    assert args.days == 7


def test_resolve_course_channel_from_metadata(tmp_path):
    course_dir = tmp_path / "llm-zoomcamp"
    course_dir.mkdir()
    (course_dir / "_metadata.yaml").write_text(
        """
course: llm-zoomcamp
course_name: LLM Zoomcamp
slack_channel: course-llm-zoomcamp
sections: []
""".strip(),
        encoding="utf-8",
    )

    assert resolve_course_channel(tmp_path, "llm-zoomcamp") == "course-llm-zoomcamp"
    assert resolve_course_channel(tmp_path, "llm-zoomcamp", "override") == "override"


def test_should_skip_empty_and_bot_messages():
    assert should_skip_slack_message({"text": ""})
    assert should_skip_slack_message({"text": "hello", "subtype": "bot_message"})
    assert not should_skip_slack_message({"text": "How do I submit homework?"})


def test_slack_ts_to_iso():
    assert slack_ts_to_iso("1710000000.000100") == "2024-03-09T16:00:00.000100+00:00"


def test_write_outputs_writes_json_and_markdown(tmp_path):
    messages = [
        SlackMessage(
            ts="1710000000.000100",
            user="U123",
            text="How do I run the notebook?",
            permalink="https://example.slack.com/archives/C1/p1710000000000100",
        ),
        SlackMessage(
            ts="1710000001.000200",
            user="U456",
            text="Use `uv run jupyter lab`.",
            thread_ts="1710000000.000100",
            permalink="https://example.slack.com/archives/C1/p1710000000000100",
        ),
    ]

    json_path, md_path = write_outputs(messages, tmp_path, "llm-zoomcamp", "course-llm-zoomcamp")

    payload = json.loads(json_path.read_text(encoding="utf-8"))
    markdown = md_path.read_text(encoding="utf-8")

    assert payload[0]["ts"] == "1710000000.000100"
    assert "Slack export: llm-zoomcamp / course-llm-zoomcamp" in markdown
    assert "thread=1710000000.000100" in markdown
    assert "Use `uv run jupyter lab`." in markdown
