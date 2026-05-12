---
id: 261ca9cbab
question: 'Git: Fatal: Authentication failed for https://github.com/username'
sort_order: 8
---

I encountered a problem when trying to push code from Git Bash:

```
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/username'
```

**Solution:**

1. Create a personal access token from your GitHub account.
2. Use this token to authenticate when you push your changes.

For more details, see the documentation on [generating a new SSH key and adding it to the SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).