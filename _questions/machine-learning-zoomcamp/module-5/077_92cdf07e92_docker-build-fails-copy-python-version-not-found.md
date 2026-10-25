---
id: 92cdf07e92
question: Docker build fails with `COPY pyproject.toml uv.lock .python-version ./`
  because `/.python-version` is not found—what’s missing?
sort_order: 77
---

You’re almost certainly missing the hidden dotfile `.python-version` (with the leading dot). It’s easy for it to get dropped/renamed when course files are downloaded individually or copied between machines.

Check the folder contents with:

```bash
ls -la
```

Look for `python-version` (without the dot) instead of `.python-version`.

Fix it by renaming:

```bash
mv python-version .python-version   # and: mv Dockerfile.txt Dockerfile
```

Verify it contains a single version string (e.g. `3.11.15`):

```bash
cat -A .python-version
```

If you see `^M` at the end (CRLF line endings), recreate it to use Unix newlines:

```bash
printf '3.11.15\n' > .python-version
```

Why this fails: Docker `COPY` stops immediately if the file doesn’t exist, so the build never reaches the later `uv`/install steps.

Related tips:
- Add a `.dockerignore` to avoid sending local artifacts to Docker every build:

```bash
printf '.venv\n__pycache__\n*.ipynb\n' > .dockerignore
```
- If multiple files were renamed/dropped, re-fetching the homework/deployment directory is often faster than fixing them one-by-one.