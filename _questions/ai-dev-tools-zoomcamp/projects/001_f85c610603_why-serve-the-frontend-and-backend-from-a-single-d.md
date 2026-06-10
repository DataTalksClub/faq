---
id: f85c610603
question: 'Why serve the frontend and backend from a single Docker container for the final project?'
sort_order: 1
---

For production and evaluation simplicity. Serving the frontend build as static files from the backend keeps requests same-origin, avoids CORS issues, and allows true end-to-end testing with a single container. During development you can still run the frontend and backend separately for faster iteration.
