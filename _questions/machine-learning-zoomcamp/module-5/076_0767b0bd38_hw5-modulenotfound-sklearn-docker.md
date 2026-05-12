---
id: 0767b0bd38
question: 'Homework 5: ModuleNotFoundError: No module named ''sklearn'' inside the Docker container'
sort_order: 76
---

The Dockerfile isn't installing dependencies into the system Python that runs at container start. With uv, in your Dockerfile you need:

```dockerfile
WORKDIR /code
COPY pyproject.toml uv.lock ./
RUN uv sync
```

The base image (`agrigorev/zoomcamp-model:2025`) has its working directory at `/code` — set `WORKDIR /code` so your `uv sync` runs there.

Also: don't `COPY pipeline_v2.bin .` — the file already exists at `/code/pipeline_v2.bin` inside the base image. Just point your loader at that path.
