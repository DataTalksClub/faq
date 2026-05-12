---
id: 28991e4581
question: 'GitHub 429: Too Many Requests when downloading a CSV via wget / pd.read_csv(url)'
sort_order: 37
---

GitHub rate-limits unauthenticated requests by IP. Workarounds:

- Wait a few minutes and retry.
- Click the "Raw" button in the browser, save the file manually, then load it from disk.
- Add a User-Agent header: `wget --user-agent="Mozilla/5.0" <url>`.
- Switch network or use a VPN.

For repeatable use, download once and commit the data file (or read from a cached local copy).
