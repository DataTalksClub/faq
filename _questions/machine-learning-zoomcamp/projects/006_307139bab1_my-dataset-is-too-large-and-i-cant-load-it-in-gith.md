---
id: 307139bab1
question: How do I fix GitHub error GH001 (file larger than 100 MiB) when pushing
  to my repo, including if the file is already in the commit history?
sort_order: 6
---

GitHub rejects a regular Git push if its history contains a file larger than 100 MiB. Choose the fix based on which commit contains the file.

To remove a file from the latest unpushed commit while keeping the local copy, run:

```bash
git rm --cached path/to/file
git commit --amend -C HEAD
```

If you add another commit, the earlier, unpushed commit will still contain the file.

If an earlier commit contains the file and you don't need it in the repository, remove it from the history with `git filter-repo`:

```bash
git filter-repo --path path/to/file --invert-paths
```

To keep the file, migrate it to Git LFS:

```bash
git lfs migrate import --everything --include="path/to/file"
```

`git filter-repo` and `git lfs migrate import` rewrite history and change commit IDs. If you already pushed the branch, coordinate with collaborators before pushing the rewritten branch with `git push --force-with-lease`. The `git lfs track` command applies only to future commits, so use `git lfs migrate import` for files already in history.

See GitHub's guides to [large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) and [removing a file from repository history](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), plus the Git LFS [migration guide](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc).
