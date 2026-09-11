#!/usr/bin/env python3
"""One trace to local Opik. UI: http://localhost:5173, project faq-automation.

  export OPIK_URL_OVERRIDE=http://localhost:5173/api OPIK_PROJECT_NAME=faq-automation
  uv run --project faq_automation python scripts/demo_opik_trace.py             # no key
  OPENAI_API_KEY=... uv run --project faq_automation python scripts/demo_opik_trace.py --live
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault("OPIK_URL_OVERRIDE", "http://localhost:5173/api")
os.environ.setdefault("OPIK_PROJECT_NAME", "faq-automation")

from opik import track  # noqa: E402


@track
def faq_proposal_triage(course: str = "llm-zoomcamp"):
    from faq_automation.rag_agent import FAQAgent

    agent = FAQAgent(Path(f"_questions/{course}"), openai_api_key="dummy")
    return agent.build_messages("How do I check my Python version?", "Run `python --version`.")


if __name__ == "__main__":
    import opik

    if "--live" in sys.argv:
        from faq_automation.rag_agent import process_faq_proposal

        d = process_faq_proposal(
            Path("_questions/llm-zoomcamp"),
            "How do I check my Python version?",
            "Run `python --version`.",
            os.environ["OPENAI_API_KEY"],
        )
        print("live:", d.action, d.section_id)
    else:
        faq_proposal_triage()
        print("dry-run trace sent")
    opik.flush_tracker()
    print("view at http://localhost:5173, project faq-automation")
