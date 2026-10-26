---
id: 9d2d5578e2
question: 'Why did my GitHub issue close automatically when I merged a PR, even though
  the PR description said "do not close #N"?'
sort_order: 17
---

GitHub can automatically close issues when it sees certain closing keywords in a PR title or description (and similarly in commit messages) followed by an issue reference.

Key points:
- The keywords are `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves`, `resolved`.
- If any of those appear immediately before an issue reference like `#8`, GitHub treats it as an instruction to close that issue when the PR merges into the default branch.
- This means phrasing like “Do not close #8 …” still closes `#8` because GitHub doesn’t interpret the surrounding negation.
- It can happen in a PR description, PR title, or the eventual commit message that lands on the default branch.

How to link the issue without closing it:
- Use `Refs #8` or `Related to #8`.
- Avoid placing any closing keyword directly before `#<number>`.

If you need the issue to stay open until QA/review, make sure your PR text uses `Refs`/`Related` (or doesn’t include the closing keywords at all).