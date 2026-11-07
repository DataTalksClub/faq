---
id: ac86a07238
question: When answering Homework 5 Question 2, why does `uv.lock` show `scikit-learn
  == 1.9.1` instead of the `1.7.2` version specified in the assignment?
sort_order: 76
---

From a shared repository, switch to `cohorts/2026/homework/05-deployment/` and run these commands to sync the lock file and check the installed version:

```bash
cd cohorts/2026/homework/05-deployment
uv sync --locked
uv run python -c 'import sklearn; print(sklearn.__version__)'
```

The `pyproject.toml` in this directory specifies `scikit-learn==1.7.2`, and `uv.lock` records version `1.7.2`. See the [Homework 5 setup instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md#setup) and the [project file](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/pyproject.toml).
