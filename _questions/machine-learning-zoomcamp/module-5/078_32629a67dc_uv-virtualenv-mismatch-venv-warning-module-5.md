---
id: 32629a67dc
question: When running scripts (e.g., `smoke_test.py` / `q6_test.py`) with `uv run
  python ...` in Module 5, I get a `VIRTUAL_ENV ... does not match ... .venv` warning—how
  do I fix it?
sort_order: 78
---

This warning means your shell has an older virtual environment activated (e.g., `venv`, `.LM`, etc.), but `uv` detects that the project has its own environment at `.venv` and decides to use that project environment instead.

To resolve it:

1. Deactivate the currently active environment, then rerun:
   - In your terminal run `deactivate` and then re-run `uv run python script.py`.

2. If you intentionally want to run using the currently active environment instead of the project’s `.venv`, target it explicitly:
   - Use `uv run --active python script.py`.

3. If the script runs successfully, you can ignore the warning:
   - `uv` will continue and run your script using the correct `.venv` environment, so the warning is not typically fatal.