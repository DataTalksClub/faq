---
id: 6ce6f7860a
question: I don’t have a credit card. Can I still deploy my final project if it has
  a separate frontend, backend API, and database?
sort_order: 6
---

Yes. You can deploy without a credit card by using provider options that don’t require payment details (or by choosing services with free tiers/trials), even if your app is split into a Vite frontend, a FastAPI backend, and a PostgreSQL database.

One workable example stack (not required) is: Vercel for the static frontend, FastAPI Cloud for the API, and Neon for PostgreSQL.

Practical steps:
- Deploy the API first.
- In the frontend, set the API base URL to the deployed backend URL.
- Update the backend’s CORS settings so the frontend’s exact origin is allowed.
- Put sensitive values (database URLs, API/signing secrets) into each provider’s secret-management system rather than in GitHub or source files.
- If your database provider offers it, use a separate development branch/environment.
- Have CI run tests and health checks, and only then deploy.

If a provider asks for card details but you don’t have one, don’t enter payment info—pick a different service.

Finally, verify end-to-end from the browser (not just by checking that URLs respond). Provider plans/payment requirements can change, so confirm current terms before signing up.