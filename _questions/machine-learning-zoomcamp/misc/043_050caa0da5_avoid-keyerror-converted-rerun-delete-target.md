---
id: 050caa0da5
question: 'How do I avoid `KeyError: ''converted''` when re-running a cell that deletes
  the target column in pandas?'
sort_order: 43
---

This happens because once you run a cell that deletes `converted` (e.g., `del df_train['converted']`), the column is removed from the dataframe. Re-running the same cell tries to delete a column that no longer exists, so pandas raises a `KeyError`.

Make the deletion safe to re-run with `drop(..., errors='ignore')`, which doesn't fail if the column is already gone:

```python
# Safe way to remove the target variable on multiple runs
df_train = df_train.drop(columns=['converted'], errors='ignore')
df_val = df_val.drop(columns=['converted'], errors='ignore')
df_test = df_test.drop(columns=['converted'], errors='ignore')
```

If you want to avoid rerun issues altogether, you can also structure your preprocessing so the "rename/drop target" step only executes once per notebook run (or reload the original dataframe before re-running).
