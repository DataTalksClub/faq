---
id: 8f85106e3b
question: How do I fix `uv add tensorflow` failing with "No solution found... all
  versions of tensorflow have no wheels with a matching Python version tag"?
sort_order: 46
---

This error usually happens because `uv` resolves dependencies for all Python versions your project allows in `pyproject.toml`, not just the Python you’re currently running. For example, if `requires-python` is set to `>=3.14`, `uv` will try to resolve TensorFlow for Python versions where TensorFlow has no matching wheels (e.g., it may only support Python 3.10–3.13 for a given TensorFlow version), so resolution fails.

Fix:

1. Update the Python constraint in `pyproject.toml` to a range TensorFlow supports, for example:

```toml
requires-python = ">=3.12,<3.13"
```

2. (Optional) Pin the interpreter (after step 1):

```bash
uv python pin 3.12
```

3. Recreate/sync the environment and add TensorFlow:

```bash
uv sync
uv add tensorflow
```

4. Verify it imports:

```bash
uv run python -c "import tensorflow as tf; print(tf.__version__)"
```

Gotchas:
- Don’t use `requires-python = "==3.12"` (that means exactly `3.12.0`; it can reject `3.12.x`). Use `">=3.12,<3.13"` or `"==3.12.*"`.
- Avoid forcing installs with `--frozen`; it won’t help if the lock/project Python requirements are incompatible.
- If you’re starting a new project, prefer the right Python version from the start: `uv init --python 3.12`.
- If you use Jupyter, make sure the kernel points to the project’s `.venv` (running `uv sync` after a Python version change may recreate it).