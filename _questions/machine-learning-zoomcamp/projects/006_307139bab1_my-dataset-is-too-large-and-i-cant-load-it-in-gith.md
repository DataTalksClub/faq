---
id: 307139bab1
question: How do I fix GitHub error GH001 (file larger than 100 MiB) when pushing
  to my repo, including if the file is already in the commit history?
sort_order: 6
---

GitHub blocks normal `git push` operations when a commit contains a file larger than 100 MiB (often shown as GH001 / “large files”). The correct fix is to remove the large file from your Git history and store it with Git LFS.

First, use Git LFS for the large file(s):

- Install Git LFS and initialize it: 
  - `git lfs install`
- Track the file pattern (example):
  - `git lfs track "path/to/large-file-or-pattern"`
- Commit the generated `.gitattributes` file, then re-add the large file and commit again.

If the large file was already committed in the past, deleting it in a later commit is not enough, because earlier commits still contain the blob. In that case, rewrite history to remove it, e.g. with `git filter-repo`:

- Example (replace the path/pattern):
  - `git filter-repo --path "path/to/large-file" --invert-paths`

After history rewriting, your local commit IDs will change, so you will typically need a force push:

- `git push --force-with-lease`

Because rewriting history changes commit IDs, coordinate with collaborators before force-pushing to a shared branch.

See GitHub docs on large files and removing files from repository history:
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository