---
id: c73cdc7714
question: FastAPI container serving fails because my AI-generated Vite frontend is
  SSR (no static `index.html`)—how do I fix it?
sort_order: 4
---

If your AI builder scaffolds your frontend with SSR (e.g., Next.js/Remix/TanStack Start or an SSR-enabled setup), the build often won’t emit a static HTML shell like `index.html`. That breaks the course’s single-container deployment approach where FastAPI serves the frontend’s static files.

Fix it by switching the frontend build to a static SPA export, then have FastAPI serve the produced static assets:

1) Update the frontend framework configuration to disable SSR and enable static SPA output.
   - For examples like `vite.config.ts` or `next.config.js`, change the config so the build exports static HTML/CSS/JS (no Node runtime required).

2) Re-generate/adjust your Dockerfile to match the “static frontend + FastAPI serves it” strategy.
   - Use a multi-stage build: Stage 1 builds the static frontend assets; Stage 2 builds a Python/FastAPI image and copies those static files into the location FastAPI serves from.

3) If your builder already generated the project, fix it via a follow-up to your agent:
   - Tell it explicitly: “The frontend must be a static SPA build (no SSR/Node runtime). Update the frontend configuration to export static assets and update the Dockerfile so FastAPI serves those assets from the root/public path.”

4) Lock the decision in `AGENTS.md` so the agent doesn’t revert later:
   - Add a single rule: “The frontend is a static SPA. Production builds must output static files to be served by FastAPI; do not introduce a Node.js server runtime.”