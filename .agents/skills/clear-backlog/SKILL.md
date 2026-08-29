---
name: clear-backlog
description: "Clear the FAQ repository backlog one item at a time: review and resolve all open pull requests first, then work through open issues. Use when the user asks to clear, review, process, or work through the FAQ PR/issue backlog. Check placement, duplicates, canonical sources, technical accuracy, and content quality; pause for approval on every item; and recommend issue eval coverage only when it protects a meaningful agent behavior."
---

# Clear the FAQ Backlog

Process all open pull requests before starting the issue queue. Work strictly
one item at a time: investigate one item, show the user the original and the
recommendation, wait for approval, resolve it, and only then show the next item.

Do not bulk-merge, bulk-close, or silently move past the approval checkpoint.

## Prepare

1. Read `AGENTS.md`, `CONTRIBUTING.md`, and the relevant course metadata.
2. Check `git status --short --branch`. Preserve unrelated user changes.
3. Fetch and prune remote refs.
4. List open PRs and issues. Process each queue oldest first unless the user
   requests another order.

## Phase 1: Pull requests

Finish the open PR queue before working on issues.

### Investigate one PR

Read the PR, diff, linked issue, and comments. Check:

- **Course and section:** confirm the section in
  `_questions/<course>/_metadata.yaml`. Module numbers differ across courses.
- **Placement:** verify the proposal against the canonical course material, not
  only its title or the submitter's selected module.
- **Duplicate coverage:** search the FAQ and all open or closed issues and PRs
  for the concepts and likely synonyms.
- **Filename and sort order:** inspect every file in the target section for
  prefix or `sort_order` collisions.
- **Accuracy:** verify changing or technical claims against the current course
  repository and authoritative primary documentation.
- **Content quality:** require a direct, concise, self-contained answer with
  runnable code and no undefined variables.
- **Relevance:** reject generic programming material and content owned by
  another course.

### Present the PR

Show only this PR:

1. Original question and answer
2. Existing or canonical coverage
3. Problems found
4. Recommended action: merge, fix then merge, merge useful details into an
   existing FAQ, or close
5. Exact proposed wording or changes

Wait for explicit user approval before editing, merging, or closing.

### Resolve the PR

For an approved fix, check out the PR branch, edit it, validate it, commit, and
push to that branch.

- If the prefix or sort order collides, move the file to the end of the section
  and update both values without asking.
- If useful details overlap an existing entry, update the existing entry and
  close the duplicate PR.
- Squash-merge accepted PRs and delete their branches.
- Closing a PR does not necessarily close its linked issue. Close or preserve
  the issue deliberately and explain why in a useful comment.
- Verify the PR and linked issue states after resolving them.

Return to the PR queue. Start issues only when no open PR remains.

## Phase 2: Issues

### Investigate one issue

Read the full issue and comments, then check:

- Existing FAQs in the selected course and likely neighboring courses
- Open and closed issues and PRs for earlier handling or duplication
- Current canonical lessons, homework, code, and configuration
- Authoritative primary documentation for technical or changing claims
- Whether the report was already fixed upstream or came from a stale checkout
- Whether the durable outcome is a new FAQ, an update, a canonical-source fix,
  a duplicate closure, a wrong-course closure, or no action

Prefer fixing an avoidable ambiguity in canonical material. Do not close a
still-valid source defect merely because it is not an FAQ task. If the source
repository is outside the authorized scope, explain the preferred source fix
and request approval before changing it.

### Decide whether it belongs in the eval set

Always include an explicit **Eval recommendation** when presenting an issue.
Recommend adding an eval only when it protects a meaningful agent behavior.

Good reasons to add an eval:

- The agent chose the wrong action, course, section, or target document.
- The issue exposes a recurring placement, retrieval, duplicate-detection, or
  content-generation failure not already represented.
- A prior correction could plausibly regress after prompt, metadata, or search
  changes.
- The expected outcome is stable and can be asserted without encoding a
  transient product fact.

Reasons not to add an eval:

- It is a straightforward FAQ addition and existing placement rules work.
- Existing cases already test the same failure mode.
- It only adds an exact self-match to increase the case count.
- The issue is stale, already fixed upstream, duplicates canonical material, or
  depends on a temporary count, version, price, or service response.

State the recommendation and concrete reasons. Do not add an eval by default.
If an eval is warranted, prefer the smallest useful layer:

- Search eval for a retrieval regression
- End-to-end eval for action, placement, target-document, or generated-content
  behavior
- Both only when both layers failed independently

Recreate historical corpus state with hidden document IDs when later FAQs would
otherwise leak the human correction. Never weaken an assertion merely to make a
noisy run pass.

### Present the issue

Show only this issue:

1. Original submission
2. Duplicate and canonical-source findings
3. Accuracy corrections
4. Recommended resolution and exact proposed content or closing comment
5. Eval recommendation, with reasons

Wait for explicit user approval before changing files or external state.

### Resolve the issue

For an approved FAQ addition or update:

1. Follow the `add-faq-record` workflow.
2. Run `stylint` on changed public prose.
3. Run `git diff --check`, `make test-website`, and focused evals only when eval
   behavior changed.
4. Stage only this issue's files.
5. Commit after each issue with the issue number in the one-line message, for
   example `"Explain delayed trace ingestion (#336)"`.
6. Synchronize with the remote, push, and close the issue.
7. Add a closing comment when it records useful reasoning, corrections, the
   canonical source, or the implemented commit. Avoid empty status comments.

If an approved resolution changes no repository files, close with the useful
comment and do not create an empty commit.

After each issue, verify the issue state, clean working tree, and remote sync
before showing the next item.

## Conventions

- FAQ path:
  `_questions/<course>/<section>/<NNN>_<10-char-hex-id>_<slug>.md`
- Match the zero-padded filename prefix to `sort_order`.
- Take section IDs and ownership from the course's `_metadata.yaml`.
- Keep one issue per commit and reference `#<issue>` in its message.
- Lead each user update with the outcome; do not rely on earlier updates for
  the final handoff.
