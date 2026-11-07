---
id: 9ee2ec921f
question: Why does docker build time out while uv sync downloads a package in Homework 5?
sort_order: 7
---

If `uv sync` times out while downloading a package during the Homework 5 image build, raise its HTTP timeout and retry count for that command:

```dockerfile
RUN UV_HTTP_TIMEOUT=120 UV_HTTP_RETRIES=5 uv sync --locked --no-dev
```

These settings give slow package downloads more time and allow more attempts. They won't fix a missing package, an invalid index, or a network that can't reach the package server. If the build still fails, check the package URL and network connection before changing `uv.lock` or dependency versions.

See the [Homework 5 container instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md#container) and the [uv HTTP environment variables](https://docs.astral.sh/uv/reference/environment/#uv_http_timeout).
