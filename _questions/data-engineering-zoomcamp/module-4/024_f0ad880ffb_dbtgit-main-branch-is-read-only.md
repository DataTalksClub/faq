---
id: f0ad880ffb
question: 'dbt + git: the main branch is "read-only" — how do I make changes?'
sort_order: 24
---

dbt Cloud (and the dbt VS Code extension) protect the main/default branch by making it read-only. To make changes, create and switch to a feature branch:

In the dbt Cloud IDE, click "create new branch" in the top-left and give it a name.

From the command line:

```bash
git checkout -b your-feature-branch
```

Make your edits, commit, push, then open a pull request to merge back to main:

```bash
git add .
git commit -m "your change description"
git push origin your-feature-branch
```

After the PR is merged on GitHub, the change appears on main.

See the dbt docs on [version control basics](https://docs.getdbt.com/docs/collaborate/git/version-control-basics) for more.
