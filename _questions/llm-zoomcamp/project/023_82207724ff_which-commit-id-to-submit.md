---
id: 82207724ff
question: Which commit should I put in the "Commit ID" field when I submit my project?
sort_order: 23
---

The commit you want reviewed — reviewers see your repo at exactly that commit
and nothing after it. In practice, push everything first, then submit the latest
commit on your main branch, so the two are the same thing.

The submission form on the course management platform shows an illustration of
where to find the 7-character commit id on GitHub. Open your repository, look at
the latest commit above the file list (or open the commits page), and copy the
short hash displayed next to it.

If you prefer the command line:

```bash
git rev-parse --short HEAD
```

Anything you commit after submitting is invisible to reviewers, since they open
`https://github.com/{username}/{repo-name}/tree/{commit-hash}` or run
`git reset --hard {commit-hash}` after cloning. If you need to change something
before the deadline, push it and update the commit id in the form.
