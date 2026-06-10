---
id: e44aaef8b7
question: "I get CORS errors locally after building the frontend. What's going on?"
sort_order: 2
---

This is the "CORS trap" with a monolith setup: if your backend disables CORS whenever it detects a `frontend/dist` folder (assuming production = same origin), a local build will fool it into blocking your localhost dev server. Don't rely on folder checks - use an explicit environment variable (e.g. `APP_ENV`) to decide prod vs dev, and configure the frontend to use relative paths (`/api`) so the production build respects the same-origin policy.
