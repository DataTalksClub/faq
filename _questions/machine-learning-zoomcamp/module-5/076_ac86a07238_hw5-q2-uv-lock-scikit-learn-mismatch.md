---
id: ac86a07238
question: When answering Homework 5 Question 2, why does `uv.lock` show `scikit-learn
  == 1.9.1` (or other unconstrained versions) instead of the homework-pinned `1.7.2`?
sort_order: 76
---

This usually happens because you’re inspecting the root repo’s `pyproject.toml`/`uv.lock` (from earlier Homeworks) instead of the isolated locked environment created for Homework 5.

Homework 5 is self-contained and expects you to use the pinned environment under `cohorts/2026/homework/05-deployment/` (or your local `05-deployment/`).

1. `cd cohorts/2026/homework/05-deployment`
2. Sync the locked environment:

   ```bash
   uv sync --locked
   ```

3. Verify that the pinned files in that same directory match the homework options:
   - `05-deployment/pyproject.toml` should list `scikit-learn==1.7.2`
   - `05-deployment/uv.lock` should show `name = "scikit-learn"` and `version = "1.7.2"`

Make sure both your terminal working directory and your editor are scoped to the `05-deployment/` folder when checking versions or running `uv` commands.