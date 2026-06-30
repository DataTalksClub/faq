---
id: bcdb8740ce
question: My homework submission is rejected because my repo URL returns a non-200
  status (e.g. 500) — how do I fix it?
sort_order: 7
---

The submission checker fetches the URL you submit with a GET request and expects an HTTP `200` response. A non-200 status (404, 500, etc.) almost always means the link isn't publicly reachable as-is. Check the usual causes:

- **Private repo** — make the repository public so the checker can access it.
- **Trailing `.git`** — submit the plain repository URL (e.g. `https://github.com/you/repo`), not `https://github.com/you/repo.git`.
- **Typo in the URL** — paste the exact link.

A quick test: open the URL in a private/incognito browser window. If it loads for you there, it'll work for the checker too.
