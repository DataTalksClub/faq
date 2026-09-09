---
id: 5648a018a2
question: 'How do I fix ModuleNotFoundError when running pytest on a src-layout project
  on Linux?'
sort_order: 13
---

When tests live in `tests/` but import a package under `src/` (e.g. `from weekly_feedback.cli import main`), plain `pytest` fails with `ModuleNotFoundError` because pytest adds the test file's directory to `sys.path`, not the project root — so the `src/` package is invisible.

Point pytest at `src` — the directory containing the importable package, not the repo root. In `pyproject.toml` (as in the Unit 1 `weekly-feedback` project):

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

Or in a `pytest.ini` at the repo root:

```ini
[pytest]
testpaths = tests
pythonpath = src
```

The `pythonpath` option needs pytest 7+. Alternatively, `pip install -e .` makes the package importable everywhere without pytest config.
