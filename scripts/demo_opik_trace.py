#!/usr/bin/env python3
"""Send one FAQ triage trace to local Opik (no OpenAI key needed for dry-run).

Local Opik must be running (../opik/./opik.sh, UI at http://localhost:5173):

  export OPIK_URL_OVERRIDE=http://localhost:5173/api
  export OPIK_WORKSPACE=default
  export OPIK_PROJECT_NAME=faq-automation

Dry-run (retrieval only, no LLM call):
  uv run python scripts/demo_opik_trace.py --dry-run

Live (calls OpenAI responses.parse, needs OPENAI_API_KEY):
  uv run python scripts/demo_opik_trace.py --course llm-zoomcamp
"""

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from faq_automation.opik_tracing import configure_opik, project_name, track  # noqa: E402


@track(project="faq-automation")
def retrieval_demo(course_dir: Path, question: str, answer: str):
    from faq_automation.rag_agent import FAQAgent

    agent = FAQAgent(course_dir, openai_api_key=os.environ.get("OPENAI_API_KEY", "dummy"))
    messages = agent.build_messages(question, answer)
    return {"num_messages": len(messages), "prompt_chars": sum(len(m["content"]) for m in messages)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", default="llm-zoomcamp")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--question", default="How do I check my Python version?")
    parser.add_argument("--answer", default="Run `python --version` in your terminal.")
    args = parser.parse_args()

    os.environ.setdefault("OPIK_URL_OVERRIDE", "http://localhost:5173/api")
    os.environ.setdefault("OPIK_WORKSPACE", "default")
    os.environ.setdefault("OPIK_PROJECT_NAME", "faq-automation")
    configure_opik()

    repo_root = Path(__file__).resolve().parents[1]
    course_dir = repo_root / "_questions" / args.course
    if not course_dir.exists():
        print(f"course dir missing: {course_dir}", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        out = retrieval_demo(course_dir, args.question, args.answer)
        print(f"dry-run trace sent to project {project_name()}: {out}")
        print("view at http://localhost:5173, project faq-automation")
        try:
            import opik

            opik.flush_tracker()
        except Exception:
            pass
        return

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not set (use --dry-run for no-LLM demo)", file=sys.stderr)
        sys.exit(1)
    from faq_automation.rag_agent import process_faq_proposal

    decision = process_faq_proposal(course_dir, args.question, args.answer, api_key)
    print(f"live trace sent: action={decision.action} section={decision.section_id}")
    print("view at http://localhost:5173, project faq-automation")
    try:
        import opik

        opik.flush_tracker()
    except Exception:
        pass


if __name__ == "__main__":
    main()
