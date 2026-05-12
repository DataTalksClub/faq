---
id: e8177805be
question: 'AttributeError: ''DataFrame'' object has no attribute ''TotalCharges'' after running the cell again'
sort_order: 30
---

You ran a cell that lowercases column names twice. After:

```python
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

the column is now `totalcharges`, not `TotalCharges`. Either:

- Reload the original dataframe before re-running the cell, or
- Split your data-prep code so the rename only runs once, or
- Make the rename idempotent: it will silently no-op the second time since the columns are already lowercase.
