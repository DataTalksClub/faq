---
id: 1f4ae0aa4b
question: When two groomed backlog issues depend on each other (cycle), should I implement
  them one at a time anyway?
sort_order: 6
---

Yes, implement in dependency order—but fix the backlog first and don’t work around a cycle.

Why it happens: the grooming/PM agent typically looks at one issue at a time, so Issue A’s acceptance criteria can assume an endpoint that Issue B will introduce, while Issue B’s constraints assume A already exists. With the “linked follow-up” rule, both issues can end up assuming the other, creating a grooming bug.

What to do:
1) Identify which issue “owns” the shared piece (usually the model or the endpoint).
2) Move that shared work into the owning issue, delete it from the other issue, and use a one-way dependency link (e.g., “blocked by #…”) instead of mutual/blocking links.
3) If they can’t be separated because they’re truly one vertical slice, merge them into a single issue and close the other as a duplicate.
4) After grooming (before implementing anything), run a quick dependency check: ask the assistant to list dependencies between all open issues and flag any cycles. Catching cycles early prevents engineers from writing code against a spec that can’t hold.

Then implement in dependency order once the cycle is removed.