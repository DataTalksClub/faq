---
id: 2922f2a648
question: 'How do I create a GitHub repository to submit my homework?'
sort_order: 5
---

You'll create a repo on GitHub, connect your local folder to it, push your code, and submit the repo link. You need Git installed and a GitHub account.

1. Create a folder (e.g. `ai-dev-tools-zoomcamp`) and put your homework files inside.
2. On github.com, create a new public repo (skip README/license for now) and click "Create repository".
3. In a terminal, move into your folder and run:
   ```
   git init
   git remote add origin https://github.com/USERNAME/ai-dev-tools-zoomcamp.git
   git remote -v
   ```
4. Add and commit your files:
   ```
   git add .
   git commit -m "Add homework for module 1"
   ```
5. Push and set tracking:
   ```
   git push -u origin main
   ```
   Future updates are just `git add .` / `git commit -m "..."` / `git push`.
6. Open your repo page on GitHub, copy the URL, and paste it into the homework submission form.
