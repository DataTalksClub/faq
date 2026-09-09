---
id: 5d234ceff9
question: 'What is AGENTS.md and how do I use it for regular commits and prompt history?'
sort_order: 9
---

`AGENTS.md` gives coding agents durable, project-specific context and instructions, so you don't repeat the same instructions in every prompt. Put the file at the repo root (see [agents.md](https://agents.md/)) and document stable project information there:

- Project structure and conventions
- Commands for running the application and tests
- Coding standards and constraints
- Important architectural decisions
- Testing and validation requirements

For example, a line like "commit code to git regularly" makes the agent commit on its own. Most assistants read `AGENTS.md` automatically (Antigravity is a notable exception). Cursor also has Commands for repetitive instructions.

Keep long-lasting rules in `AGENTS.md`; task-specific requirements belong in the spec or backlog rather than in `AGENTS.md`.

To keep prompt history, save the agent's plan files (e.g. `PLAN.md` / `todo.md`) or export your chat - handy when you switch models or revert code. See the [Unit 1 lesson](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/cohorts/2026/01-ai-native-workflow/lesson.md) for how specs, backlogs, and `AGENTS.md` fit into the AI-native workflow.
