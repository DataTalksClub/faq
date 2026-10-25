---
id: d800d8e9c1
question: 'KeyError: ''[...] not in index'' when using KFold on df_full_train—how
  do I fix it?'
sort_order: 10
---

This happens when you use `KFold.split()` indices with `.loc`.

- `KFold.split(df_full_train)` returns integer row positions (`0 .. n-1`), not the DataFrame’s index labels.
- `.loc[...]` uses index labels, so it can raise `KeyError` (label not found) or silently select the wrong rows.

Fix options:

1) Use `.iloc` with the fold indices:

```python
import pandas as pd
from sklearn.model_selection import train_test_split, KFold

df = pd.read_csv('course_lead_scoring_2026.csv')
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

kfold = KFold(n_splits=5, shuffle=True, random_state=1)

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]
```

2) Or reset the index so labels match positions before splitting:

- add `df_full_train = df_full_train.reset_index(drop=True)` before the `kfold.split(...)` loop.

Either approach ensures you select the intended train/validation rows for each fold.