---
id: cc0048eefb
question: '''403 Forbidden'' error message when you try to push to a GitHub repository'
sort_order: 7
---

To resolve a '403 Forbidden' error when pushing to a GitHub repository, follow these steps:

1. Check the current remote URL configuration by running:

   ```bash
   git config -l | grep url
   ```

   The output should be similar to:

   ```
   remote.origin.url=https://github.com/github-username/github-repository-name.git
   ```

2. Change the URL format to include your GitHub username:

   ```bash
   git remote set-url origin "https://github-username@github.com/github-username/github-repository-name.git"
   ```

3. Verify the change is reflected using the command in step 1. Make sure the URL is correctly updated.