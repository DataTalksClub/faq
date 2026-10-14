---
id: c73cdc7714
question: My AI-generated frontend (Lovable, v0, Bolt) uses SSR and the build has
  no static `index.html` for FastAPI to serve. How do I fix it?
sort_order: 4
---

If your AI builder scaffolds your frontend with SSR (e.g., Next.js/Remix/TanStack Start or an SSR-enabled setup), the build often won’t emit a static HTML shell like `index.html`. That breaks the course’s single-container deployment approach where FastAPI serves the frontend’s static files.

Fix it by switching the frontend build to a static SPA export, then have FastAPI serve the produced static assets:

1) Ask the agent to switch the framework to static/SPA output (for example TanStack Start's SPA mode or Next.js `output: 'export'`), then confirm `npm run build` produces an `index.html` in the output directory.

2) Re-generate/adjust your Dockerfile to match the “static frontend + FastAPI serves it” strategy.
   - Use a multi-stage build: Stage 1 builds the static frontend assets; Stage 2 builds a Python/FastAPI image and copies those static files into the location FastAPI serves from.

3) If your builder already generated the project, fix it via a follow-up to your agent:
   - Tell it explicitly: “The frontend must be a static SPA build (no SSR/Node runtime). Update the frontend configuration to export static assets and update the Dockerfile so FastAPI serves those assets from the root/public path.”

4) Lock the decision in `AGENTS.md` so the agent doesn’t revert later:
   - Add a single rule: “The frontend is a static SPA. Production builds must output static files to be served by FastAPI; do not introduce a Node.js server runtime.”
