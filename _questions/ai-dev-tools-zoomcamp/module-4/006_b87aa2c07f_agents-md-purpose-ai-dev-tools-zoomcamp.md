---
id: b87aa2c07f
question: What is `AGENTS.md` used for in the AI Dev Tools Zoomcamp?
sort_order: 6
---

`AGENTS.md` is used to give coding agents durable, project-specific context and instructions.

Instead of repeating the same instructions in every prompt, you can document stable project information in `AGENTS.md`, such as:
- Project structure and conventions
- Commands for running the application and tests
- Coding standards and constraints
- Important architectural decisions
- Testing and validation requirements
- Guidance the coding agent should follow when modifying the project

This is especially helpful in an AI-native workflow: the agent can read reliable instructions up front before implementing items from the backlog.

A good `AGENTS.md` should focus on long-lasting project rules (general constraints and conventions). Task-specific requirements should stay in the spec or backlog rather than in `AGENTS.md`.