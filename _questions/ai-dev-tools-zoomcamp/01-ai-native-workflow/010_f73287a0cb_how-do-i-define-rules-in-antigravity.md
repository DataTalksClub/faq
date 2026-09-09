---
id: f73287a0cb
question: 'How do I define rules in Antigravity?'
sort_order: 10
---

Rules in Antigravity are Markdown files with standards, conventions, and constraints that guide the agent. You can manage them through the UI or by creating the files directly — see the [official Rules docs](https://antigravity.google/docs/rules-workflows).

To use the UI: open the Customizations panel via the "…" dropdown at the top of the agent panel, go to the Rules panel, and click + Global or + Workspace.

### Workspace rules

Workspace rules live in the `.agents/rules` folder of your workspace or git root. Create a `.md` file there (e.g. `coding-standards.md`) with your constraints in plain Markdown. (The older `.agent/rules` path still works, but `.agents/rules` is the current default.)

### Global rules

Global rules apply across all workspaces and live in `~/.gemini/GEMINI.md`.

At the rule level you can set how a rule activates: Manual (via @ mention in the agent input), Always On, Model Decision (the model decides from your description), or Glob (applies to files matching a pattern like `src/**/*.ts`).
