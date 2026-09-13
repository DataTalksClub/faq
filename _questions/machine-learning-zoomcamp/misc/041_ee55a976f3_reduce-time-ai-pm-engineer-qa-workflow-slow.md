---
id: ee55a976f3
question: How can I reduce the time taken by an AI PM/Engineer/QA agent workflow when
  everything feels slow?
sort_order: 41
---

If your multi-agent workflow feels slow, try to reduce loops and unnecessary work:

- Keep the task list focused: too few tasks can miss coverage, but too many can create stalls or “infinite” churn. Aim for a manageable number and group tasks logically.
- Ask the orchestrator (PM/manager agent) to review the plan against CRISP-DM/“robust process” criteria, but also explicitly challenge whether the process is overkill for a simple project to avoid bloat.
- Add explicit checks before starting: have the AI review the tasks and issues to catch logical loops, anomalies, or missing dependencies.
- Use a hierarchy of agents/models: instruct the orchestrator to be a higher-capability LLM, while the coding/doer agents use smaller/faster LLM tiers.
- Give the orchestrator time-control and monitoring guidance so it doesn’t let sub-agents run unattended or indefinitely.
- For the coding agent, use a “lazy ponytail” style of incremental development (start with the simplest correct approach, then refine) to avoid unnecessary refactors.
- Run a short dry run first and closely monitor sub-agent behavior; early surfaced anomalies often save hours during the full run.

Once these checks “pass,” you can run the complete process with more confidence and less rework.