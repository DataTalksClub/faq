---
id: 8eb3018dba
question: How do I use `GridSearchCV` with parallel processing, and how do I fix the
  scikit-learn parallel-processing warning?
sort_order: 35
---

`GridSearchCV` uses `cv` cross-validation to evaluate many parameter combinations and picks the one with the best score. To parallelize the work, set `n_jobs=-1`.

Example:

```python
from sklearn.model_selection import GridSearchCV

gs = GridSearchCV(
    est, grid, scoring="roc_auc", cv=cv, n_jobs=-1
)
gs.fit(X_train, y_train)
```

Why you see a parallel-processing warning

When you run `GridSearchCV` with parallel workers, scikit-learn may emit a warning like:

```text
UserWarning: `sklearn.utils.parallel.delayed` should be used with
`sklearn.utils.parallel.Parallel` to make it possible to propagate
the scikit-learn configuration of the current thread to the joblib workers.
```

This warning is about how scikit-learn configuration is propagated to joblib workers. By itself, it does not necessarily mean your dataset, model, or `roc_auc` computation is wrong.

If the warning persists, try one of these fixes:

1) Targeted warning filter

```python
import warnings

warnings.filterwarnings(
    "ignore",
    message=r".*sklearn\.utils\.parallel\.delayed.*",
    category=UserWarning,
)
```

2) Enable context-aware warning handling at Python startup

Some environments handle warning filters differently when parallel code runs. If filtering doesn’t suppress the warning, enable context-aware warning handling when starting Python.

For JupyterLab (run from your project directory, after stopping any existing server):

```bash
PYTHON_CONTEXT_AWARE_WARNINGS=1 uv run jupyter lab
```

For Jupyter Notebook:

```bash
PYTHON_CONTEXT_AWARE_WARNINGS=1 uv run jupyter notebook
```

Check whether it’s enabled:

```python
import sys

print(sys.flags.context_aware_warnings)
```

If it prints `1`, the setting is active.

Note: this environment variable must be set when Python starts; setting it inside an already-running notebook won’t have the same effect.