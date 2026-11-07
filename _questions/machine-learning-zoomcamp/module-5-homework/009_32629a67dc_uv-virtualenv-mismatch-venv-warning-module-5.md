---
id: 32629a67dc
question: How do I fix the VIRTUAL_ENV warning when running Homework 5 scripts with uv?
sort_order: 9
---

When you run `uv run` in a project, `uv` uses the project's environment by default. If `VIRTUAL_ENV` is set to a different environment, `uv` warns that it will ignore that environment.

To remove the warning, deactivate the old environment and run the homework command again:

```bash
deactivate
uv run python smoke_test.py
```

If you intentionally want to run a command in the active environment, pass `--active`:

```bash
uv run --active python smoke_test.py
```

The warning tells you which environment `uv` selected. It doesn't mean the script failed. See the [Homework 5 setup instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md#setup) and [uv's project environment documentation](https://docs.astral.sh/uv/concepts/projects/config/#project-environment-path).
