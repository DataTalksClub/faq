#!/usr/bin/env python3
"""Fetch recent Slack channel activity for manual FAQ curation."""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from .core import read_metadata


SLACK_API_BASE = "https://slack.com/api"
DEFAULT_COURSE = "llm-zoomcamp"


class SlackAPIError(RuntimeError):
    """Raised when Slack returns an unsuccessful API response."""


@dataclass
class SlackMessage:
    """A normalized Slack message used for FAQ review."""

    ts: str
    user: str
    text: str
    thread_ts: str | None = None
    permalink: str | None = None


def load_env_file(path: Path) -> None:
    """Load simple KEY=VALUE pairs from a local .env file."""
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", maxsplit=1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def slack_api_call(token: str, method: str, params: dict[str, str | int | float | bool]) -> dict:
    clean_params = {key: value for key, value in params.items() if value != ""}
    query = urllib.parse.urlencode(clean_params)
    request = urllib.request.Request(
        f"{SLACK_API_BASE}/{method}?{query}",
        headers={"Authorization": f"Bearer {token}"},
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise SlackAPIError(f"Slack HTTP error for {method}: {e.code} {detail}") from e
    except urllib.error.URLError as e:
        raise SlackAPIError(f"Could not call Slack {method}: {e}") from e

    if not payload.get("ok"):
        raise SlackAPIError(f"Slack API error for {method}: {payload.get('error', 'unknown_error')}")

    return payload


def resolve_channel_id(token: str, channel: str, include_private: bool = False) -> str:
    """Resolve a channel name or ID to a Slack channel ID."""
    clean = channel.strip()
    if clean.startswith("#"):
        clean = clean[1:]
    if clean[:1] in {"C", "G"} and clean.isupper():
        return clean

    channel_types = "public_channel"
    if include_private:
        channel_types += ",private_channel"

    cursor = ""
    while True:
        payload = slack_api_call(
            token,
            "conversations.list",
            {
                "types": channel_types,
                "exclude_archived": "true",
                "limit": 1000,
                "cursor": cursor,
            },
        )
        for item in payload.get("channels", []):
            if item.get("name") == clean:
                return item["id"]

        cursor = payload.get("response_metadata", {}).get("next_cursor", "")
        if not cursor:
            break

    raise SlackAPIError(f"Could not find Slack channel: {channel}")


def fetch_channel_messages(
    token: str,
    channel_id: str,
    oldest: float,
    limit: int,
    include_threads: bool = True,
) -> list[SlackMessage]:
    """Fetch recent Slack messages and optionally include thread replies."""
    messages: list[SlackMessage] = []
    cursor = ""

    while len(messages) < limit:
        payload = slack_api_call(
            token,
            "conversations.history",
            {
                "channel": channel_id,
                "oldest": oldest,
                "limit": min(200, limit - len(messages)),
                "cursor": cursor,
            },
        )

        for item in payload.get("messages", []):
            if should_skip_slack_message(item):
                continue

            root = to_slack_message(item)
            root.permalink = get_permalink(token, channel_id, root.ts)
            messages.append(root)

            if include_threads and item.get("reply_count", 0) > 0:
                messages.extend(fetch_thread_replies(token, channel_id, root.ts, root.permalink))

            if len(messages) >= limit:
                break

        cursor = payload.get("response_metadata", {}).get("next_cursor", "")
        if not cursor:
            break

    return sorted(messages, key=lambda m: float(m.ts))


def fetch_thread_replies(
    token: str,
    channel_id: str,
    thread_ts: str,
    permalink: str | None,
) -> list[SlackMessage]:
    payload = slack_api_call(
        token,
        "conversations.replies",
        {"channel": channel_id, "ts": thread_ts, "limit": 200},
    )
    replies = []
    for item in payload.get("messages", [])[1:]:
        if should_skip_slack_message(item):
            continue
        reply = to_slack_message(item)
        reply.thread_ts = thread_ts
        reply.permalink = permalink
        replies.append(reply)
    return replies


def get_permalink(token: str, channel_id: str, message_ts: str) -> str | None:
    try:
        payload = slack_api_call(
            token,
            "chat.getPermalink",
            {"channel": channel_id, "message_ts": message_ts},
        )
    except SlackAPIError:
        return None
    return payload.get("permalink")


def should_skip_slack_message(item: dict) -> bool:
    if item.get("subtype") in {"channel_join", "channel_leave", "bot_message"}:
        return True
    return not item.get("text", "").strip()


def to_slack_message(item: dict) -> SlackMessage:
    return SlackMessage(
        ts=item["ts"],
        user=item.get("user") or item.get("username") or "unknown",
        text=item.get("text", "").strip(),
        thread_ts=item.get("thread_ts"),
    )


def slack_ts_to_iso(ts: str) -> str:
    return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()


def resolve_course_channel(questions_dir: Path, course: str, channel_override: str | None = None) -> str:
    """Read the Slack channel for a course from its metadata."""
    if channel_override:
        return channel_override

    course_dir = questions_dir / course
    if not course_dir.exists():
        raise ValueError(f"Course directory does not exist: {course_dir}")

    metadata = read_metadata(course_dir)
    channel = metadata.get("slack_channel")
    if not channel:
        raise ValueError(f"No slack_channel configured in {course_dir / '_metadata.yaml'}")
    return channel


def write_outputs(
    messages: list[SlackMessage],
    output_dir: Path,
    course: str,
    channel: str,
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_channel = channel.strip("#").replace("/", "-")
    stamp = datetime.now(tz=timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = output_dir / f"slack-{course}-{safe_channel}-{stamp}.json"
    md_path = output_dir / f"slack-{course}-{safe_channel}-{stamp}.md"

    json_path.write_text(
        json.dumps([asdict(message) for message in messages], indent=2),
        encoding="utf-8",
    )

    lines = [f"# Slack export: {course} / {channel}", ""]
    for message in messages:
        thread = f" thread={message.thread_ts}" if message.thread_ts else ""
        permalink = f" {message.permalink}" if message.permalink else ""
        lines.append(f"## {slack_ts_to_iso(message.ts)} user={message.user}{thread}{permalink}")
        lines.append("")
        lines.append(message.text)
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def run_fetch(args: argparse.Namespace) -> int:
    load_env_file(Path(".env"))

    slack_token = os.environ.get("SLACK_BOT_TOKEN")
    if not slack_token:
        print("Error: SLACK_BOT_TOKEN is not set in .env or the environment", file=sys.stderr)
        return 1

    try:
        channel = resolve_course_channel(Path(args.questions_dir), args.course, args.channel)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    try:
        channel_id = resolve_channel_id(slack_token, channel, include_private=args.include_private)
    except SlackAPIError as e:
        print(f"Error: {e}", file=sys.stderr)
        print(
            "The Slack app needs Bot Token scopes for reading channels. "
            "For a public course channel, add channels:read and channels:history, "
            "then reinstall the app to the workspace. For private channels, also add "
            "groups:read and pass --include-private.",
            file=sys.stderr,
        )
        return 1

    oldest = int(time.time() - (args.days * 24 * 60 * 60))

    print(f"Fetching Slack messages from {channel} for {args.course}, last {args.days} days...")
    try:
        messages = fetch_channel_messages(
            slack_token,
            channel_id,
            oldest=oldest,
            limit=args.limit,
            include_threads=not args.no_threads,
        )
    except SlackAPIError as e:
        print(f"Error: {e}", file=sys.stderr)
        print(
            "The Slack app needs history access for this channel. "
            "For public channels use channels:history; for private channels use groups:history "
            "and make sure the app is a channel member.",
            file=sys.stderr,
        )
        return 1

    json_path, md_path = write_outputs(messages, Path(args.output_dir), args.course, channel)

    print(f"Fetched {len(messages)} message(s).")
    print(f"JSON: {json_path}")
    print(f"Markdown: {md_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fetch recent Slack channel activity for manual FAQ curation.",
    )
    parser.add_argument(
        "--channel",
        default=None,
        help="Slack channel name or ID. Overrides the course metadata.",
    )
    parser.add_argument("--course", default=DEFAULT_COURSE, help="Course directory under _questions")
    parser.add_argument("--questions-dir", default="_questions", help="FAQ questions directory")
    parser.add_argument("--days", type=int, default=7, help="How many days of Slack history to fetch")
    parser.add_argument("--limit", type=int, default=500, help="Maximum Slack messages to fetch")
    parser.add_argument("--output-dir", default=".tmp", help="Directory for exported Slack data")
    parser.add_argument("--no-threads", action="store_true", help="Do not fetch thread replies")
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="Allow channel-name lookup across private channels. Requires groups:read.",
    )
    return parser


def main() -> None:
    load_env_file(Path(".env"))
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(run_fetch(args))


if __name__ == "__main__":
    main()
