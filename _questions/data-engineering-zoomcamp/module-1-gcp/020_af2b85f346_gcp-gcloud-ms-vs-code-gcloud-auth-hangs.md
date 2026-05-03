---
id: af2b85f346
question: GCP gcloud + MS VS Code - gcloud auth hangs
sort_order: 20
---

If you are using MS VS Code and running `gcloud` in WSL2, when you first try to login to GCP via the `gcloud` CLI with `gcloud auth application-default login`, you may encounter an issue where the terminal prints a long OAuth URL and then shows a series of "not found" errors for browsers:

```
Your browser has been opened to visit:
    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=...

/usr/bin/xdg-open: 882: x-www-browser: not found
/usr/bin/xdg-open: 882: firefox: not found
/usr/bin/xdg-open: 882: chromium: not found
...
xdg-open: no method available for opening '...'
```

VS Code may show a notification: "Your application running on port 8085 is available" with an "Open in Browser" button. Clicking it may lead to an error page.

**Solution:**

1. Hover over the long OAuth URL in the terminal output.
2. `Ctrl + Click` the link — VS Code will show a dialog: "Do you want Code to open the external website?" with buttons **Open**, **Copy**, **Configure Trusted Domains**, and **Cancel**.
3. Click **Configure Trusted Domains**.
4. A dropdown will appear with options like:
   - "Trust https://accounts.google.com"
   - "Trust google.com and all its subdomains"
   - "Trust all domains (disables link protection)"
   - "Manage Trusted Domains"
5. Pick the first or second entry (e.g., "Trust https://accounts.google.com").

Next time you run `gcloud auth`, the login page should pop up via the default browser without issues.