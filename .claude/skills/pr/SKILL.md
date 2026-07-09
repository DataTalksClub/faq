---
name: pr
description: Review and process open FAQ pull requests one by one — check placement, duplicates, sort_order collisions, and content quality, then merge or close. Use when the user wants to go through open FAQ PRs or review proposed FAQ entries.
---

# Review FAQ Pull Requests

Review and process open FAQ pull requests **one at a time**: show the details, check
placement / relevance / duplicates / quality, fix what's fixable, merge or close, then
move to the next.

Start with `gh pr list --state open` to see the queue.

## 1. Review each PR

For each PR (pull details with `gh pr view <N>` and `gh pr diff <N>`):

- **Course & section**: confirm the section exists in `_questions/<course>/_metadata.yaml`.
  Section ids and module numbers **differ per course** — never assume a module number maps
  to a topic across courses. For example, in `llm-zoomcamp` Kestra/orchestration is
  `module-3`; in `data-engineering-zoomcamp` it's `module-2`. Always check the metadata.
- **sort_order & filename prefix collision**: this is the most common bot bug. List the
  target section (`ls _questions/<course>/<section>/`) and check whether the PR's `NNN_`
  prefix and `sort_order` already exist. If they collide, renumber (see step 2).
- **Duplicate**: search `_questions/<course>/` for the topic (`rg -i "keyword"`). If an
  existing entry already answers it, close as duplicate.
- **Content quality**: is the code runnable? Are undefined variables used? Is the answer
  accurate and concise per `CONTRIBUTING.md`? Verify claims against the real course repo
  or documentation — don't trust the proposed answer's framing.
- **Relevance**: close if the question is generic programming not tied to course content,
  basic tutorials, or belongs to a different course.

## 2. Fix before merging

Check out the branch (`gh pr checkout <N>`), make the fixes, commit, and push back to the
PR branch.

### Renumbering (do it silently)

If the prefix or sort_order collides with an existing file, move the file to the **end** of
the section — the next number after the current highest in that directory. Update both the
`NNN_` filename prefix and `sort_order` in the frontmatter.

- **Do not ask the user** if it fits at the end — just renumber.
- **Only ask the user** if the new entry needs to go somewhere other than the end, i.e. if
  reordering existing questions would make sense.

### Content fixes

- Fix code: add missing definitions, make examples self-contained, correct syntax.
- Clean up formatting: fix broken markdown, add trailing newline.
- Trim verbose or generic text down to a concrete, concise answer.

### Merge useful content into existing entry

If the PR has some value but duplicates an existing entry, merge anything worthwhile into
the existing entry, then close the PR and the issue.

When committing on a checked-out PR branch, run `git status` first to confirm you are only
staging the FAQ file you edited.

## 3. Merge or close

- **Merge** (squash, delete branch): `gh pr merge <N> --squash --delete-branch`. The PR
  body's `Closes #<issue>` auto-closes the related issue on merge.
- **Close** (duplicate or not relevant): closing a PR does NOT auto-close its linked
  issue, so handle both:
  1. `gh pr close <N> --delete-branch --comment "Closing — already covered by <existing entry>."`
  2. `gh issue close <issue> --comment "Closing — this is already covered by <existing entry>."`

  The comment should point to the specific existing FAQ that covers the topic, e.g.
  "already covered by the existing entry 'Which AI providers does Kestra support besides
  Gemini?' (module-3, file `006_f442efe5b4_...`)."

After each PR, verify the related issue is actually closed (`gh issue view <N> --json
state`). Prune stale remote tracking refs with `git fetch --prune`.

## Conventions reference

- File format: `_questions/<course>/<section>/<NNN>_<id>_<slug>.md` where `NNN` = sort_order
  (zero-padded to 3 digits) and `<id>` is the 10-char doc id from frontmatter.
- Frontmatter: `id`, `question`, `sort_order`.
- Section ids and names come from `_questions/<course>/_metadata.yaml`.
- Writing guidelines: `CONTRIBUTING.md` — direct answer first, code examples when relevant,
  concise but complete, markdown formatting.
