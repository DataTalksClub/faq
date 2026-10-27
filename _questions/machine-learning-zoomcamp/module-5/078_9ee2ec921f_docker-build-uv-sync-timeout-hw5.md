---
id: 9ee2ec921f
question: Why does `docker build` fail with a timeout when running `uv sync --locked
  --no-dev` in Homework 5?
sort_order: 78
---

If your Docker build fails with something like:

Failed to download `some-package`
Request failed after 3 retries
operation timed out

a common fix is to increase `uv`’s HTTP timeout and retry count during the `uv sync` step in your `Dockerfile`.

Replace:

```dockerfile
RUN uv sync --locked --no-dev
```

with something like:

```dockerfile
RUN UV_HTTP_TIMEOUT=120 UV_HTTP_RETRIES=5 uv sync --locked --no-dev
```

Then rebuild the image from the homework directory:

```bash
docker build -t zoomcamp-model:2026-hw5 .
```

Why this happens: during the Docker build, `uv` may take longer to download dependencies from PyPI than its default HTTP timeout allows, even if the package/version exists. Increasing the timeout/retries gives downloads more time and allows additional attempts.

If it still fails, try isolating the root cause:
- Test the package URL with `curl`
- Check your network connection
- Avoid changing `uv.lock` or dependency versions unless you confirm the problem is a specific dependency issue