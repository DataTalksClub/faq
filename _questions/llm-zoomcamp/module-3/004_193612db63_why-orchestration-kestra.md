---
id: 193612db63
question: Why do we need orchestration / Kestra — can't I just run the code in a notebook?
sort_order: 4
---

Notebooks are great for learning and experimenting, but real AI workflows need more than a script that runs once: scheduling, retries, monitoring, secret management, and reliably chaining tasks together. That's what an orchestrator like Kestra provides.

In this module Kestra is also the vehicle for the AI techniques the course is teaching: AI Copilot to generate flows from natural language, RAG to ground responses in real data, and AI agents that decide which tools to call. The goal is to see how AI fits into production-style workflows, not just notebook cells.

Kestra's AI plugins also work with any major provider (OpenAI, Gemini, Anthropic, and more), so you can swap providers in a flow without changing anything else. See the [module intro](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/03-orchestration/lessons/01-intro.md) for the full motivation.
