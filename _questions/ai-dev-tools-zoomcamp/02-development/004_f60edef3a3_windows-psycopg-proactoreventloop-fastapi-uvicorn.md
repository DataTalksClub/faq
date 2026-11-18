---
id: f60edef3a3
question: On Windows, my FastAPI backend (SQLAlchemy async + psycopg 3) fails with
  “Psycopg cannot use the 'ProactorEventLoop' to run in async mode”. How do I fix
  it?
sort_order: 4
---

psycopg 3 in async mode doesn’t support Windows’ default `ProactorEventLoop`, and `uvicorn` uses that loop on Windows. If it works in Docker/Linux and CI but fails only on native Windows, switch the server to an async-compatible event loop.

Pick one fix:

1) Run `uvicorn` on a selector event loop
Create a loop factory and pass it to `uvicorn`.

```python
# app/event_loop.py
import asyncio

def new_event_loop() -> asyncio.AbstractEventLoop:
    return asyncio.SelectorEventLoop()
```

Run:

```bash
uv run uvicorn app.main:app --reload --loop app.event_loop:new_event_loop
```

2) Run the backend in Docker (or WSL)
For example:

```bash
docker compose up --build
```

3) Use the sync PostgreSQL driver (if you can)
If you don’t need async DB access, switch from the async `psycopg` URL/engine to the sync `postgresql+psycopg://` setup.

Note: setting `asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())` inside your app module is often too late, because `uvicorn` may create the event loop before your module code runs. The `--loop` factory approach is usually the most reliable.