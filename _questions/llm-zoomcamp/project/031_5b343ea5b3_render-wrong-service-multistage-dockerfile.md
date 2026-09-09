---
id: 5b343ea5b3
question: Why did Render deploy the wrong service from my multi-stage Dockerfile?
sort_order: 31
---

Render builds your Dockerfile with no `--target` flag (its Blueprint spec has no field to select a build stage), and a target-less `docker build` always produces the stage declared last. If your `Dockerfile` has multiple stages — e.g. an `api` stage and a `ui` stage sharing a base — whichever comes last is what Render runs. Reordering stages or appending a new one silently changes what gets deployed: the build still succeeds, it just ships the wrong image.

This is easy to miss locally because `docker-compose` sets `target:` per service, so the same Dockerfile behaves correctly under compose while deploying the wrong thing on Render:

```dockerfile
FROM python:3.11-slim AS deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# UI stage — deliberately NOT last
FROM deps AS ui
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]

# `api` is deliberately the LAST stage: Render builds with no --target,
# and a target-less build resolves to whichever stage comes last.
# DO NOT append new stages below this one.
FROM deps AS api
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
services:
  api:
    build: { context: ., target: api }
  ui:
    build: { context: ., target: ui }
```

To keep it fixed: keep the deployed service as the last stage and verify by hitting a route unique to that service (not a shared `/health` endpoint both services might answer identically). Before pushing, reproduce Render's target-less build locally:

```bash
docker build -t check .  # no --target, same as Render
docker run --rm -p 8010:8000 check
curl -s localhost:8010/health
```

See [Render's Docker docs](https://docs.render.com/docker) — multi-stage builds are supported, but there is no target-stage selection.
