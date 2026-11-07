---
id: 6ce6f7860a
question: I don’t have a credit card. Can I still deploy my final project if it has a separate frontend, backend API, and database?
sort_order: 7
---

Yes, you can use separate providers if their current free plans and signup requirements fit your project. You might host a Vite frontend on Vercel, the API on FastAPI Cloud, and PostgreSQL on Neon. Your course doesn't require this stack.

Check each provider's current limits and terms before signing up. FastAPI Cloud currently lists its Hobby plan as free with no credit card required. Vercel's Hobby plan is for personal, non-commercial use. If a provider asks for payment details you don't want to give, choose another service.

After deploying, set the frontend's API URL to the backend address and allow the frontend's deployed origin in the backend's CORS settings. Store database URLs and signing keys in the providers' secret settings, not in the repository. See the current [FastAPI Cloud plans](https://fastapicloud.com/pricing/), [Vercel Hobby terms](https://vercel.com/docs/plans/hobby), and [Neon plans](https://neon.com/docs/introduction/plans).
