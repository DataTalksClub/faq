---
id: aa92a4f1b1
question: How do I deploy my Dockerized API to Render (free tier)?
sort_order: 77
---

Quickest path:

1. Push your image to Docker Hub:
   ```bash
   docker push <your-username>/<image>:latest
   ```
2. In Render, create a new Web Service → "Deploy an existing image from a registry" → paste the Docker Hub URL.
3. Set the start command (e.g. `uvicorn predict:app --host 0.0.0.0 --port $PORT`). Render injects `$PORT` at runtime — listen on it, don't hardcode.
4. Free tier sleeps after ~15 min idle, so the first request after that takes ~30s to wake up.

Render is the most popular free-tier choice for this course's project deployment because it doesn't require a credit card. Other options: Fly.io, Google Cloud Run (both require a card), Railway, PythonAnywhere.

Don't post Docker Hub itself as your "deployment" — it's a registry, not a runtime.
