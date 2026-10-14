---
id: 7eb51be644
question: "Playwright installed Chromium, but my coding agent still can't open a page. Why, and what should I do?"
sort_order: 1
---

`npx playwright install chromium` only downloads the browser binary into a user cache. Chromium also needs OS-level shared libraries (NSS, GBM, fonts, audio). Those are installed by `npx playwright install --with-deps chromium` (or `npx playwright install-deps`), which calls the system package manager and needs root. In a sandbox without sudo that step can't run, so the binary is on disk but fails to launch. The launch error lists the exact missing libraries.

What to do:

1. If you have root (`id -u` prints `0`, or `sudo -n true` succeeds), run:

   ```bash
   npx playwright install --with-deps chromium
   ```

   If you control the container, use Playwright's official Docker image, which already includes the browsers and their dependencies.

2. Otherwise, check the connection yourself: start the backend and the frontend, open the app in your browser, and watch the Network tab. The homework allows manual verification.

3. As a fallback, the agent can check the API contract and CORS with `curl`, sending the `Origin` header your browser would send (adjust ports and routes):

   ```bash
   curl -i -X OPTIONS http://localhost:8000/api/items \
     -H "Origin: http://localhost:5173" \
     -H "Access-Control-Request-Method: POST"
   ```

   The response must contain `access-control-allow-origin` matching your frontend origin. This is weaker than a browser test, so make sure the agent reports that no real browser check happened.

See [Playwright: install system dependencies](https://playwright.dev/docs/browsers#install-system-dependencies).
