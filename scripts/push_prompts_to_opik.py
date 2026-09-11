#!/usr/bin/env python3
"""Version our prompts in the Opik Prompt Library (without using them from there).

Single source of truth stays faq_automation/rag_agent.py — this script only
mirrors SYSTEM_PROMPT and PROMPT_TEMPLATE into Opik so every version is
stored next to the traces and experiments that used it. Re-running with
unchanged templates creates nothing (Opik versions on diff).

Respects OPIK_URL_OVERRIDE / OPIK_WORKSPACE / OPIK_PROJECT_NAME / OPIK_API_KEY.

Usage:
  source .env
  # Cloud:
  OPIK_URL_OVERRIDE=https://www.comet.com/opik/api OPIK_WORKSPACE=default \\
    OPIK_PROJECT_NAME=faq-automation-ci \\
    uv run --project faq_automation python scripts/push_prompts_to_opik.py
  # Local (http://localhost:5173):
  OPIK_PROJECT_NAME=faq-automation \\
    uv run --project faq_automation python scripts/push_prompts_to_opik.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault("OPIK_URL_OVERRIDE", "http://localhost:5173/api")
os.environ.setdefault("OPIK_WORKSPACE", "default")
os.environ.setdefault("OPIK_PROJECT_NAME", "faq-automation-ci")

PROMPTS = [
    ("faq-triage-system",
     "System prompt: triage rules for NEW/UPDATE/DUPLICATE/WRONG_COURSE.",
     "SYSTEM_PROMPT"),
    ("faq-triage-user-template",
     "User prompt template: course, catalog, entry, search results, sections.",
     "PROMPT_TEMPLATE"),
]


def main():
    from opik import Opik
    from faq_automation.rag_agent import DEFAULT_MODEL
    import faq_automation.rag_agent as rag

    project = os.environ.get("OPIK_PROJECT_NAME", "faq-automation-ci")
    client = Opik(project_name=project)
    for name, description, attr in PROMPTS:
        template = getattr(rag, attr)
        prompt = client.create_prompt(
            name=name,
            prompt=template,
            description=description,
            metadata={"source": "faq_automation/rag_agent.py:" + attr,
                      "format": "python-str-format",
                      "model": DEFAULT_MODEL},
            tags=["faq-automation", "triage"],
            project_name=project,
        )
        print(f"{name}: commit {prompt.commit} ({project})")


if __name__ == "__main__":
    main()
