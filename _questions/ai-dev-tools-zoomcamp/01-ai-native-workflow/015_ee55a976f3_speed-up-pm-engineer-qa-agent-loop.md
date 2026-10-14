---
id: ee55a976f3
question: How can I speed up the PM / Engineer / QA orchestrator loop?
sort_order: 15
---

The orchestrated loop is slow by design. Every issue goes through grooming, implementation and QA as separate subagent runs, and the lesson notes that it "takes significantly more time and tokens than a direct loop with only a software engineer." To speed it up:

- Skip the full loop for small or simple projects. A single engineer agent, or a plain prompt, is often enough.
- Keep issues small but not tiny. Group related work so each issue is one reviewable slice. Dozens of micro-issues multiply the PM and QA overhead.
- Before you start the loop, ask the assistant to review the backlog for dependency cycles and unclear acceptance criteria. Those are what cause FAIL -> reimplement churn.
- Run the subagents on a faster or cheaper model, and keep the stronger model for the orchestrator or PM if your tool supports per-agent models.
- Do a dry run on one issue and watch what each subagent does before you run `/goal work through the backlog`.
