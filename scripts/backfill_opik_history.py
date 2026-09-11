#!/usr/bin/env python3
"""Backfill FAQ-proposal history into Opik as traces with real timestamps.

For each `faq-proposal` issue, logs one `faq-proposal-triage` trace:
  - input:  the original issue (course/question/answer) + retrieval context
    REGENERATED with the current search code (mirrors rag_agent retrieval)
  - output: the ACTUAL historical decision read from the bot PR
    ([FAQ Bot] NEW/UPDATE + merged file) or the bot close comment
    (DUPLICATE / WRONG_COURSE), or MANUAL when a human decided
  - start_time: issue created_at, end_time: PR created / comment / closed at

Nothing is re-decided by an LLM: this is history, not an eval. No new
dependencies (gh CLI + stdlib + existing project deps). Secrets come from
the environment (source .env first), never from code.

Usage:
  source .env  # OPIK_API_KEY (OPENAI_API_KEY not needed)
  uv run --project faq_automation python scripts/backfill_opik_history.py --dry-run
  OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \\
    OPIK_PROJECT_NAME=faq-automation-ci \\
    uv run --project faq_automation python scripts/backfill_opik_history.py --limit 30
"""

import argparse
import datetime
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

os.environ.setdefault("OPIK_URL_OVERRIDE", "http://localhost:5173/api")
os.environ.setdefault("OPIK_WORKSPACE", "default")
os.environ.setdefault("OPIK_PROJECT_NAME", "faq-automation-ci")


def sh(*args):
    out = subprocess.run(["gh", *args], capture_output=True, text=True, check=True)
    return json.loads(out.stdout or "null")


def new_id():
    try:
        return str(uuid.uuid7())  # type: ignore[attr-defined]
    except AttributeError:
        ms = time.time_ns() // 1_000_000
        v = ((ms << 80) | (7 << 76) | (random.getrandbits(12) << 64)
             | (0b10 << 62) | random.getrandbits(62))
        return str(uuid.UUID(int=v))


def post_traces(traces, base, workspace, api_key):
    payload = {"traces": traces}
    headers = {"content-type": "application/json", "Comet-Workspace": workspace}
    if api_key:
        headers["authorization"] = api_key
    req = urllib.request.Request(base.rstrip("/") + "/v1/private/traces/batch",
                                 data=json.dumps(payload).encode(),
                                 method="POST", headers=headers)
    with urllib.request.urlopen(req, timeout=30):
        pass


def parse_pr_outcome(number):
    """Find the bot PR for an issue. Returns dict or None."""
    prs = sh("pr", "list", "--head", f"faq-bot/issue-{number}",
             "--state", "all", "--json", "number,title,createdAt,url") or []
    if not prs:
        return None
    pr = prs[0]
    action = "NEW" if "[FAQ Bot] NEW" in pr["title"] else (
        "UPDATE" if "[FAQ Bot] UPDATE" in pr["title"] else "NEW")
    files = sh("pr", "view", str(pr["number"]), "--json", "files")["files"]
    section, document_id, pr_path = "", "", ""
    if files:
        pr_path = files[0]["path"]
        parts = pr_path.split("/")
        if len(parts) >= 4 and parts[0] == "_questions":
            section = parts[2]
            name = parts[3].split("_", maxsplit=2)
            if len(name) >= 2 and len(name[1]) == 10:
                document_id = name[1]
    return {"action": action, "section": section, "document_id": document_id,
            "pr_path": pr_path,
            "pr_number": pr["number"], "pr_url": pr["url"], "decided_at": pr["createdAt"]}


def parse_comment_outcome(comments):
    """Find the bot close comment. Returns dict or None."""
    for c in comments or []:
        body = c.get("body") or ""
        if body.startswith("## 🔄 Duplicate FAQ Entry"):
            doc, section = "", ""
            for line in body.splitlines():
                if line.startswith("**Document ID**:"):
                    doc = line.split("`")[1] if "`" in line else ""
                if line.startswith("**Section**:"):
                    section = line.split(":", 1)[1].strip()
            return {"action": "DUPLICATE", "section": section, "document_id": doc,
                    "comment_url": c.get("url", ""), "decided_at": c.get("createdAt", "")}
        if body.startswith("## 📚 Wrong Course"):
            return {"action": "WRONG_COURSE", "section": "", "document_id": "",
                    "comment_url": c.get("url", ""), "decided_at": c.get("createdAt", "")}
    return None


def read_file_content(course, pr_path, document_id, pr_number=None):
    """Rewrite content: the merged file (NEW/UPDATE) or matched entry (DUPLICATE).

    Current file content approximates what the system generated — the merged
    record is the rewrite. For closed-unmerged bot PRs the file never landed
    on main, so fall back to the PR diff (the bot proposal). Best-effort:
    empty string when unresolvable.
    """
    from faq_automation.core import find_question_files

    candidates = []
    if pr_path:
        candidates.append(ROOT / pr_path)
    if document_id:
        try:
            index = find_question_files(ROOT / "_questions" / course)
            if document_id in index:
                candidates.append(index[document_id])
        except Exception:
            pass
    for path in candidates:
        try:
            if path.exists():
                return path.read_text()[:4000]
        except Exception:
            continue
    if pr_number:
        try:
            out = subprocess.run(["gh", "pr", "diff", str(pr_number)],
                                 capture_output=True, text=True, check=True, cwd=ROOT)
            lines = []
            for line in out.stdout.splitlines():
                if line.startswith("+++ ") or line.startswith("--- ") or \
                   line.startswith("diff ") or line.startswith("index ") or \
                   line.startswith("@@") or line.startswith("new file"):
                    continue
                if line.startswith("+"):
                    lines.append(line[1:])
            if lines:
                return "\n".join(lines)[:4000]
        except Exception:
            pass
    return ""


def retrieval_context(course, question, answer, hide_doc_ids, _cache={}):
    """Real retrieval output shape, regenerated with current search code."""
    from faq_automation.core import keep_relevant, reciprocal_rank_fusion
    from faq_automation.rag_agent import FAQAgent

    key = (course, tuple(sorted(hide_doc_ids)))
    if key not in _cache:
        course_dir = ROOT / "_questions" / course
        if hide_doc_ids:
            tmp = Path(tempfile.mkdtemp()) / course
            shutil.copytree(course_dir, tmp)
            for f in tmp.glob("*/*.md"):
                parts = f.name.split("_", maxsplit=2)
                if len(parts) >= 2 and parts[1] in hide_doc_ids:
                    f.unlink()
            course_dir = tmp
        _cache[key] = FAQAgent(course_dir, openai_api_key="dummy",
                               questions_dir=ROOT / "_questions")
    agent = _cache[key]
    proposal = f"## {question}\n\n{answer}"
    both = [agent.index.search(question, num_results=10),
            agent.index.search(proposal, num_results=10)]
    results = keep_relevant(reciprocal_rank_fusion(both, weights=[1.0, 2.0], limit=5))
    # Keep match info only (id/question/section/score): full answer bodies bloat
    # the trace input ~5KB and bury the actual post in the UI. Full texts live
    # in the FAQ files; the question + score tell the retrieval story.
    keep = ("document_id", "question", "section_id", "score")
    return [{k: r[k] for k in keep if k in r} for r in results]


def build_trace(issue, outcome):
    from faq_automation.cli import parse_full_issue_body

    number = issue["number"]
    try:
        course, question, answer = parse_full_issue_body(issue.get("body") or "")
    except ValueError:
        return None, f"issue #{number}: unparseable body"
    if not (ROOT / "_questions" / course).exists():
        return None, f"issue #{number}: unknown course {course!r}"

    hide = {outcome["document_id"]} if outcome["action"] == "NEW" and outcome.get("document_id") else set()
    try:
        results = retrieval_context(course, question, answer, hide)
    except Exception as e:
        return None, f"issue #{number}: retrieval failed: {e}"

    end = outcome.get("decided_at") or issue.get("closedAt") or issue["createdAt"]
    rewrite = ""
    if outcome["action"] in ("NEW", "UPDATE", "DUPLICATE"):
        rewrite = read_file_content(course, outcome.get("pr_path", ""),
                                    outcome.get("document_id", ""),
                                    outcome.get("pr_number"))
    trace = {
        "id": new_id(),
        "project_name": os.environ.get("OPIK_PROJECT_NAME", "faq-automation-ci"),
        "name": "faq-proposal-triage",
        "start_time": issue["createdAt"],
        "end_time": end,
        "input": {"issue_number": number, "issue_url": issue.get("url", ""),
                  "course": course, "question": question, "answer": answer,
                  "search_results": results},
        "output": {"action": outcome["action"], "section": outcome.get("section", ""),
                   "document_id": outcome.get("document_id", ""),
                   "rewrite": rewrite,
                   "pr_number": outcome.get("pr_number"), "pr_url": outcome.get("pr_url", ""),
                   "comment_url": outcome.get("comment_url", "")},
        "metadata": {"backfilled": True, "source": "github-history",
                     "retrieval": "regenerated with current search code"},
        "tags": ["backfill", "github-history", course],
    }
    return trace, None


def main():
    parser = argparse.ArgumentParser(description="Backfill issue history to Opik")
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--project", default=os.environ.get(
        "OPIK_PROJECT_NAME", "faq-automation-ci"))
    parser.add_argument("--base-url", default=os.environ.get(
        "OPIK_URL_OVERRIDE", "http://localhost:5173/api"))
    args = parser.parse_args()

    os.environ["OPIK_PROJECT_NAME"] = args.project
    issues = sh("issue", "list", "--label", "faq-proposal", "--state", "all",
                "--limit", str(args.limit),
                "--json", "number,title,body,createdAt,closedAt,url") or []
    print(f"{len(issues)} issues")

    traces, skipped = [], []
    for issue in issues:
        number = issue["number"]
        try:
            full = sh("issue", "view", str(number), "--comments",
                      "--json", "number,title,body,createdAt,closedAt,url,comments")
        except subprocess.CalledProcessError as e:
            skipped.append(f"#{number}: gh failed: {e}")
            continue
        outcome = parse_pr_outcome(number) or parse_comment_outcome(full.get("comments"))
        if outcome is None:
            if full.get("closedAt"):
                outcome = {"action": "MANUAL", "decided_at": full["closedAt"]}
            else:
                skipped.append(f"#{number}: open, no decision yet")
                continue
        trace, err = build_trace(full, outcome)
        if err:
            skipped.append(err)
            continue
        traces.append(trace)
        print(f"#{number}: {trace['output']['action']} "
              f"{trace['output']['section']} <- {trace['start_time']}")

    print(f"\nready: {len(traces)}, skipped: {len(skipped)}")
    for s in skipped:
        print("  skip:", s)
    if args.dry_run or not traces:
        return
    api_key = os.environ.get("OPIK_API_KEY")
    if not api_key:
        sys.exit("OPIK_API_KEY not set (source .env first)")
    post_traces(traces, args.base_url, os.environ.get("OPIK_WORKSPACE", "default"), api_key)
    print(f"logged {len(traces)} traces to {args.project}")


if __name__ == "__main__":
    main()
