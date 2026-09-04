---
id: 9a1eef9e91
question: Claude Code login fails in GitHub Codespaces with “localhost refused to
  connect” — how do I fix it?
sort_order: 6
---

Claude Code’s OAuth login opens a browser tab pointing at `http://localhost:PORT/callback`. In GitHub Codespaces, that callback URL can fail to load because the browser reaches it through Codespaces’ port-forwarding proxy instead of talking directly to the listener.

Workaround:
1. Run `claude` and let it open the login link in your browser.
2. When the page fails to load, copy the full callback URL from the address bar (for example `http://localhost:35251/oauth/callback?code=...`).
3. In a second terminal tab inside the same Codespace, run:

```bash
curl "http://localhost:35251/oauth/callback?code=..."
```

4. Your original `claude` terminal should log in immediately.

Why this works: the `curl` runs inside the Codespace on the same machine as the listener, so it bypasses the forwarding proxy.

If this still doesn’t resolve it, check Anthropic’s “Troubleshoot installation and login” docs for other known causes.