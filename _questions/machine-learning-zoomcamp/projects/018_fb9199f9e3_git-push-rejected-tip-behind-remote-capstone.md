---
id: fb9199f9e3
question: Git push fails with “Updates were rejected because the tip of your current
  branch is behind its remote counterpart” when submitting the capstone project
sort_order: 18
---

This happens when your local `main` branch and `origin/main` have diverged (for example, you edited something like `README.md` on GitHub’s web UI while also making local commits). Git won’t push because it can’t fast-forward.

Fix (merge remote into your local history):
1. Pull the remote changes using merge (not rebase):

```bash
git pull origin main --no-rebase
```

2. If you get merge conflicts, resolve them by opening the conflicting file(s) and removing the conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>>`). In VS Code, the Source Control panel typically shows quick actions like “Accept Current Change / Accept Incoming Change / Accept Both”.

3. Commit the merge and push:

```bash
git add <file>
git commit -m "Merge origin/main"
git push origin main
```

If you’re sure your local version should win and you don’t want to resolve conflicts manually, you can pull while preferring your local changes:

```bash
git pull origin main --no-rebase --strategy-option=ours
git push origin main
```

Use this with caution: it can silently discard conflicting remote changes. After pushing, double-check the merged file (e.g., your README) to ensure nothing important was lost.