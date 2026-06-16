---
id: f3a92e7c81
question: 'minsearch: SyntaxError "invalid character" when running my downloaded
  copy'
sort_order: 15
---

```
SyntaxError: invalid character '·' (U+00B7)
```

You probably saved the GitHub HTML page instead of the raw Python file. Either:

- Use the "Raw" button on GitHub, or download from the `raw.githubusercontent.com` URL.
- Or just install from PyPI — it's the recommended path:

```bash
pip install -U minsearch
# or
uv add minsearch
```
