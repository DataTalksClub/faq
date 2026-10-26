---
id: 5f63c3735c
question: The project form asks for a commit ID, but my project has many commits.
  Which one do I submit?
sort_order: 7
---

Submit only one commit ID: the latest commit on the branch you want evaluated (usually `main`). A commit ID points to the repository state at that moment, including all earlier commits.

If you push additional changes before the deadline, update the form with the new latest commit.

You can find the latest commit ID on GitHub via the repo’s “Commits” page, or locally with:

```bash
git log -1 --format=%h
```