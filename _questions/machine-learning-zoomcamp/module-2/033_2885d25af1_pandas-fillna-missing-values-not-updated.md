---
id: 2885d25af1
question: Why are there still missing values after I use `fillna()` in Pandas?
sort_order: 33
---

By default, Pandas operations like `fillna()` don’t modify the original DataFrame in-place; they return a modified copy. If you don’t assign that result back, the missing values remain.

Fix: assign the returned Series/column back, e.g.:
- `df['score'] = df['score'].fillna(fill_value)`

Alternative: you can write into the existing data by using `inplace=True`, e.g.:
- `df['score'].fillna(fill_value, inplace=True)`

Example:
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"score": [100, np.nan, 150]})
fill_value = 0

# INCORRECT: change is lost because the result isn't assigned
df["score"].fillna(fill_value)
print(df["score"].isnull().sum())  # 1

# CORRECT: reassign the column
df["score"] = df["score"].fillna(fill_value)
print(df["score"].isnull().sum())  # 0
```