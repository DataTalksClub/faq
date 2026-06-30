#!/usr/bin/env python3
"""Fetch recent Telegram announcement-channel activity for manual FAQ curation.

Mirrors ``slack_fetch.py`` but reads each course's *public* Telegram broadcast
channel through the keyless ``t.me/s/<channel>`` web preview, so no bot token or
API key is required. Only public channels expose this preview.

Ported from faq-assistant's archived Telegram source loader; the parsing logic
(``parse_telegram_page`` / ``telegram_html_to_text``) is unchanged, the project
plumbing was rewritten to match faq_automation conventions (argparse CLI, course
metadata lookup, ``.tmp`` JSON+Markdown exports, stdlib-only HTTP).
"""

import argparse
import html as html_lib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .core import read_metadata


TELEGRAM_PREVIEW_BASE = "https://t.me/s/"
TELEGRAM_LINK_BASE = "https://t.me/"
# Telegram serves an empty preview to some default user agents; use a browser-like one.
TELEGRAM_USER_AGENT = "Mozilla/5.0 (compatible; faq-automation-ingest/1.0)"
DEFAULT_COURSE = "llm-zoomcamp"


class TelegramError(RuntimeError):
    """Raised when the Telegram preview cannot be fetched or parsed."""


@dataclass
class TelegramPost:
    """A normalized Telegram post used for FAQ review."""

    id: str
    ts: str
    title: str
    text: str
    url: str


def clean_text(value: str) -> str:
    """Collapse runs of whitespace while preserving paragraph breaks."""
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    # Collapse 3+ newlines to a blank line; trim trailing spaces per line.
    value = re.sub(r"[ \t]+\n", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def fetch_url(url: str, params: dict | None = None) -> str:
    query = f"?{urllib.parse.urlencode(params)}" if params else ""
    request = urllib.request.Request(
        f"{url}{query}",
        headers={"User-Agent": TELEGRAM_USER_AGENT},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise TelegramError(f"Telegram HTTP error: {e.code} {detail}") from e
    except urllib.error.URLError as e:
        raise TelegramError(f"Could not reach Telegram: {e}") from e


def fetch_telegram_posts(channel: str, cutoff: datetime, max_pages: int = 200) -> list[TelegramPost]:
    """Walk the t.me preview backwards with ?before=<id> until posts predate cutoff."""
    collected: dict[str, dict] = {}
    before: int | None = None

    for _ in range(max_pages):
        params = {"before": before} if before else None
        html_text = fetch_url(f"{TELEGRAM_PREVIEW_BASE}{channel}", params)

        posts = parse_telegram_page(html_text, channel)
        if not posts:
            break

        reached_cutoff = False
        for post in posts:
            if post["datetime"] < cutoff:
                reached_cutoff = True
                continue
            collected[post["id"]] = post

        if reached_cutoff:
            break
        before = min(post["seq"] for post in posts)

    ordered = sorted(collected.values(), key=lambda post: post["seq"])
    return [
        TelegramPost(
            id=post["id"],
            ts=post["datetime"].isoformat(),
            title=telegram_title(post["text"]),
            text=post["text"],
            url=f"{TELEGRAM_LINK_BASE}{post['id']}",
        )
        for post in ordered
    ]


def parse_telegram_page(html_text: str, channel: str) -> list[dict]:
    anchors = list(re.finditer(rf'data-post="{re.escape(channel)}/(\d+)"', html_text))
    posts: list[dict] = []

    for index, anchor in enumerate(anchors):
        seq = int(anchor.group(1))
        end = anchors[index + 1].start() if index + 1 < len(anchors) else len(html_text)
        segment = html_text[anchor.end() : end]

        time_match = re.search(r'<time datetime="([^"]+)"', segment)
        if not time_match:
            continue
        posted_at = datetime.fromisoformat(time_match.group(1))

        text_match = re.search(r'tgme_widget_message_text[^>]*>(.*?)</div>', segment, re.DOTALL)
        text = telegram_html_to_text(text_match.group(1)) if text_match else ""
        if not text:
            continue  # media-only / empty post

        posts.append({"id": f"{channel}/{seq}", "seq": seq, "datetime": posted_at, "text": text})

    return posts


def telegram_html_to_text(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.IGNORECASE)
    # Preserve links as Markdown so the answer can cite the real URL.
    fragment = re.sub(
        r'<a\b[^>]*\bhref="([^"]+)"[^>]*>(.*?)</a>',
        lambda m: f"[{strip_tags(m.group(2))}]({m.group(1)})",
        fragment,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return clean_text(html_lib.unescape(strip_tags(fragment)))


def telegram_title(text: str, limit: int = 80) -> str:
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
    if len(first_line) > limit:
        first_line = first_line[: limit - 1].rstrip() + "…"
    return first_line or "Telegram post"


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value)


def resolve_course_channel(questions_dir: Path, course: str, channel_override: str | None = None) -> str:
    """Read the Telegram channel for a course from its metadata."""
    if channel_override:
        return channel_override.lstrip("@")

    course_dir = questions_dir / course
    if not course_dir.exists():
        raise ValueError(f"Course directory does not exist: {course_dir}")

    metadata = read_metadata(course_dir)
    channel = metadata.get("telegram_channel")
    if not channel:
        raise ValueError(
            f"No telegram_channel configured in {course_dir / '_metadata.yaml'} "
            f"(or pass --channel)"
        )
    return str(channel).lstrip("@")


def write_outputs(posts: list[TelegramPost], output_dir: Path, course: str, channel: str) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_channel = channel.replace("/", "-")
    stamp = datetime.now(tz=timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = output_dir / f"telegram-{course}-{safe_channel}-{stamp}.json"
    md_path = output_dir / f"telegram-{course}-{safe_channel}-{stamp}.md"

    json_path.write_text(
        json.dumps([asdict(post) for post in posts], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    lines = [f"# Telegram export: {course} / @{channel}", ""]
    for post in posts:
        lines.append(f"## {post.ts} {post.url}")
        lines.append("")
        lines.append(post.text)
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def run_fetch(args: argparse.Namespace) -> int:
    try:
        channel = resolve_course_channel(Path(args.questions_dir), args.course, args.channel)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    print(f"Fetching Telegram posts from @{channel} for {args.course}, last {args.days} days...")
    try:
        posts = fetch_telegram_posts(channel, cutoff)
    except TelegramError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    json_path, md_path = write_outputs(posts, Path(args.output_dir), args.course, channel)

    print(f"Fetched {len(posts)} post(s).")
    print(f"JSON: {json_path}")
    print(f"Markdown: {md_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fetch recent Telegram channel activity for manual FAQ curation.",
    )
    parser.add_argument("--channel", default=None, help="Telegram channel handle. Overrides course metadata.")
    parser.add_argument("--course", default=DEFAULT_COURSE, help="Course directory under _questions")
    parser.add_argument("--questions-dir", default="_questions", help="FAQ questions directory")
    parser.add_argument("--days", type=int, default=365, help="How many days of Telegram history to fetch")
    parser.add_argument("--output-dir", default=".tmp", help="Directory for exported Telegram data")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(run_fetch(args))


if __name__ == "__main__":
    main()
