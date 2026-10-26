---
id: 92cdf07e92
question: Docker build fails with `COPY pyproject.toml uv.lock .python-version ./`
  because `/.python-version` is not found—what’s missing?
sort_order: 77
---

The hidden file `.python-version` (with the leading dot) is missing from your build context. It often gets dropped or renamed to `python-version` when files are downloaded one by one or copied between machines.

Check the folder, including hidden files:

```bash
ls -la
```

If you see `python-version` without the dot, rename it:

```bash
mv python-version .python-version
```

If the file is missing, recreate it with the Python version your project uses, for example:

```bash
printf '3.11\n' > .python-version
```

Docker `COPY` fails as soon as one of the listed files doesn't exist, so the build never reaches the `uv` install steps.
