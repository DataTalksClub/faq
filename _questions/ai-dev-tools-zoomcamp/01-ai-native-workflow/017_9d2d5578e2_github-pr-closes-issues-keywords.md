---
id: 9d2d5578e2
question: 'Why did my GitHub issue close automatically when I merged a PR, even though the PR description said "do not close #123"?'
sort_order: 17
---

GitHub closes a linked issue after you merge a pull request into the default branch. The PR description or a commit message on that branch must contain a closing keyword followed by the issue number. A PR title doesn't close an issue.

For example, `Closes #123` closes issue #123. The text `Don't close #123` still contains `close #123`, so GitHub treats it as a closing reference. See [GitHub's documentation on linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue).

To link an issue without closing it, write `Refs #123` or `Related to #123` in the PR description.
