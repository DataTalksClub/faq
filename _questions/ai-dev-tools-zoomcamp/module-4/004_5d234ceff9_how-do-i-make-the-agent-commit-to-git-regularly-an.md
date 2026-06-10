---
id: 5d234ceff9
question: 'How do I make the agent commit to git regularly and keep track of my prompts?'
sort_order: 4
---

Put project rules in an `AGENTS.md` file at the repo root (see https://agents.md/) - for example a line like "commit code to git regularly". Most assistants read `AGENTS.md` automatically (Antigravity is a notable exception). Cursor also has Commands for repetitive instructions. To keep prompt history, save the agent's plan files (e.g. `PLAN.md` / `todo.md`) or export your chat - handy when you switch models or revert code.
