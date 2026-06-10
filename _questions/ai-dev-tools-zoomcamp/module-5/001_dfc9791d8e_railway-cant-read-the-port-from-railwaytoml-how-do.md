---
id: dfc9791d8e
question: "Railway can't read the port from railway.toml. How do I fix it?"
sort_order: 1
---

Instead of relying on `railway.toml`, ask an AI assistant to create an entrypoint script that runs the app with uvicorn (rather than `fastapi run`). Example entrypoint:
```
exec uv run uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
```
