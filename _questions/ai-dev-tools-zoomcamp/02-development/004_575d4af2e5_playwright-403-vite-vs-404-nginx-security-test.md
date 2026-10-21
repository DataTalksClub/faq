---
id: 575d4af2e5
question: Why does a Playwright security test return HTTP 403 instead of the expected
  HTTP 404 when using Vite rather than production Nginx?
sort_order: 4
---

When you run Playwright against the development frontend (Vite), you can get different HTTP status codes than in production (Nginx) because the request routing and security logic differ between environments.

In the production setup, Nginx is configured to intercept access to private routes and return a `404` for blocked requests. In the Vite-based development setup, some requests are instead forwarded (e.g., via Vite dev proxy) to the API/backend. If the backend (or its auth/security middleware) blocks the request, it may return `403 Forbidden` because it’s making an authorization decision rather than pretending the route doesn’t exist.

How to verify what’s happening:
- Compare the request flow in both environments (Dev: Vite/proxy → API; Prod: client → Nginx → (blocked/rewritten or passed to backend)).
- In Playwright, log the failing request URL and method, then check the backend logs (or middleware/auth logs) to see whether the backend is responsible for the `403`.
- Inspect your Nginx rules for private routes to confirm they rewrite/deny with `404`, and inspect your dev/proxy config to confirm which requests bypass Nginx.

What to do:
- Update the test expectation to match the environment-appropriate behavior (often: `403` for authorization failures vs `404` when hiding private routes).
- Or make dev behavior consistent with prod by aligning the dev proxy/backend behavior with Nginx’s rule (e.g., translate `403` to `404` for the same private-route patterns, or ensure the dev stack uses the same blocking layer).