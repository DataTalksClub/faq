---
id: c745f48092
question: Codex CLI asks for approval every time it runs a GitHub CLI command. How
  do I stop approving the same command repeatedly?
sort_order: 6
---

When Codex CLI prompts for approval, it’s because the command pattern matches a rule that requires user confirmation.

- If you trust the command, choose the prompt option like “Yes, and don’t ask again for commands that start with …”. Codex will save an execution rule for that command prefix, so future matching `gh ...` commands run without asking again.

- For example, instead of approving `gh issue view 1 --json number,title,body,state,labels,url,comments` every time, select “Yes, and don’t ask again” and Codex will allow that matching `gh issue view ...` prefix for future runs.

- If you want Codex to manage approval prompting more interactively, start it with `codex --ask-for-approval on-request` so approval is controlled on demand rather than being fully disabled.

Note: “trusted project”/sandbox trust and “ask-for-approval” are separate—trusting a project doesn’t automatically disable all command-approval prompts. Avoid using `codex --ask-for-approval never` unless you understand the security implications.