---
id: 65cbd9be62
question: After uv add, uv.lock has the package but pyproject.toml shows empty dependencies = []
sort_order: 75
---

Run `uv sync` after `uv add` to reconcile `pyproject.toml` and `uv.lock`. Don't manually edit `dependencies` if `uv.lock` already has them — `uv sync` (or rerunning `uv add`) is the right fix.

Make sure you're running `uv add` from the directory that contains your `pyproject.toml`.
