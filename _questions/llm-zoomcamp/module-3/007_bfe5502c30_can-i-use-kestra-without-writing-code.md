---
id: bfe5502c30
question: Can I use Kestra without writing any code? Is there a no-code option?
sort_order: 7
---

Yes. You have three options that require no hand-written YAML or code:

- **The no-code form editor** builds a flow from a form instead of YAML. It is form-based (not drag-and-drop like n8n), so it suits people who don't want to edit YAML directly.
- **The AI Copilot** generates a flow from a natural-language description, and you can iterate with follow-up messages to add tasks or change the order. See the [AI Copilot lesson](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/03-orchestration/lessons/04-ai-copilot.md).
- **External agent skills** (Claude Code, Codex, Kestra CTL) let you generate flows and push them into Kestra from your editor without touching the Kestra UI.

Unlike Airflow, where business logic and orchestration logic are intertwined in Python, Kestra keeps the two separate: your Python script stays a plain script, and the workflow YAML just describes how and when to run it. This is closer to a cron job than to a traditional Airflow DAG.

For simple point-to-point automations (e.g. "post a Slack message when a YouTube video goes live"), a tool like Zapier or n8n may be simpler and cheaper. Kestra's advantage is observability, retries, and handling more complex or technical workflows in one place.
