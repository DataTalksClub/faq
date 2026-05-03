---
id: dc06a38bc6
question: How do I use Git / GitHub for this course?
sort_order: 24
---

After you create a GitHub account, clone the course repo to your local machine using the process outlined in this video:

[Git for Everybody: How to Clone a Repository from GitHub](https://www.youtube.com/watch?v=CKcqniGu3tA).

Having this local repository on your computer will make it easy to access the instructors’ code and make pull requests if you want to add your own notes or make changes to the course content.

You will probably also create your own repositories to host your notes and versions of files. Here is a great tutorial that shows you how to do this:

[How to Create a Git Repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository).

Remember to ignore large databases, .csv, and .gz files, and other files that should not be saved to a repository. Use `.gitignore` for this:

[.gitignore file](https://www.atlassian.com/git/tutorials/saving-changes/gitignore).

**Important:**

**NEVER store passwords or keys in a git repo** (even if the repo is set to private). Put files containing sensitive information (.env, secret.json, etc.) in your `.gitignore`.

This is also a great resource: [Dangit, Git!?!](https://dangitgit.com/)