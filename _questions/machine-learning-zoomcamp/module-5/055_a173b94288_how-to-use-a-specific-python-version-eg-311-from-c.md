---
id: a173b94288
question: 'Pipenv: how do I use a specific Python version (e.g. 3.11)?'
sort_order: 55
---

Use `uv` to install the Python version you want, then point `pipenv` at that interpreter:

```bash
# Install Python 3.11 via uv
uv python install 3.11

# Find the path uv installed it to
uv python find 3.11

# Tell pipenv to use that interpreter
pipenv --python /path/to/python3.11
```

Alternatively, if your OS package manager already has Python 3.11 (e.g. `apt install python3.11`, `brew install python@3.11`), pass that path directly to `pipenv --python`.

Avoid running `pipenv` from inside another venv — let it manage its own environment.
