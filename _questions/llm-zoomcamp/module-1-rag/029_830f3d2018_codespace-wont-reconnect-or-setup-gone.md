---
id: 830f3d2018
question: My Codespace won't reconnect (stuck on "Finishing up") or my setup has disappeared
  — what should I do?
sort_order: 29
---

These are usually GitHub Codespaces reliability issues rather than a problem with the course, so there's no single guaranteed fix — but the following workarounds resolve most cases.

**Codespace won't connect / stuck on "Finishing up":**

- Go to [github.com/codespaces](https://github.com/codespaces), stop the codespace, and start it again.
- If it still won't connect, open it in the **browser** instead of desktop VS Code, or try a different browser (Edge/Chrome/Brave).
- As a last resort, delete the codespace and create a new one.

**"My setup is all gone":**

- The repo in `/workspaces` persists across stop/start, but a **rebuild or a brand-new codespace** starts from a clean image, and system/global installs outside your project don't always survive. Reinstalling is quick with `uv` (`uv sync` / `uv add ...`).
- **Commit and push your work often** — uncommitted changes survive a stop/start but are lost if you delete or recreate the codespace.

If Codespaces keeps being flaky for you, consider running the course locally instead — see "[Can I run the course locally instead of Codespaces?](026_aa310de435_can-i-run-the-course-locally-instead-of-codespaces.md)".
