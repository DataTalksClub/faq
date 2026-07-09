---
id: cce328db64
question: Is Kestra mandatory for the LLM Zoomcamp course, or can I use another orchestrator?
sort_order: 5
---

No. Kestra is the orchestrator the course teaches in Module 3, but it is not a requirement beyond that module's homework.

For the **capstone project** you are not restricted in technology: you can use Airflow, Prefect, Dagster, or no orchestrator at all. A plain Python script that ingests and indexes your data is enough for full points on the ingestion-pipeline criterion (a Jupyter notebook with the same steps is worth 1 point instead of 2). See the [project guidelines](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md) for details.

The course uses Kestra in Module 3 because it is the vehicle for the AI techniques being taught — AI Copilot for generating flows, RAG for grounding responses, and AI agents that call tools. Other orchestrators cover the same scheduling/retry/monitoring ground, but they won't map onto those specific lessons, so it's worth running the Kestra flows at least once. If you already know Airflow (or another tool) and want to compare, give Kestra a try for the module and then use whatever fits your project best.

Kestra's AI plugins also work with any major provider (OpenAI, Gemini, Anthropic, and more), so you can swap providers in a flow without changing anything else — see the [supported providers list](https://kestra.io/plugins/plugin-ai/provider).
