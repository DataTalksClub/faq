---
id: 9bd2b3c09d
question: How do I create an empty GitHub repository, clone it, add files, commit,
  and push?
sort_order: 6
---

Do this step-by-step from your terminal:

1. Create a local folder (or use your existing project folder).

2. Create an empty repository on GitHub:
   - Go to GitHub → New repository.
   - Choose public/private.
   - Create it without adding a README (so it stays “empty”).

3. Clone the empty repo to your machine:
   - Copy the repo URL from GitHub (HTTPS).
   - Run:

   ```bash
   git clone https://github.com/USERNAME/REPO.git
   cd REPO
   ```

   (If your code is already in another folder, you can instead `git init` there, but cloning is the simplest for a truly empty repo.)

4. Copy (or move) your files into the cloned folder (the `REPO/` directory).

5. Stage files:

   ```bash
   git add .
   ```

6. Commit:

   ```bash
   git commit -m "Add project files"
   ```

7. Push to GitHub (replace `main` if your branch name differs):

   ```bash
   git push -u origin main
   ```

If you hit an authentication prompt on push, use the credentials method recommended by GitHub (now typically a GitHub token instead of a password).