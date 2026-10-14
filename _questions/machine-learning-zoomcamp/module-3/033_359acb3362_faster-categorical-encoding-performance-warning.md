---
id: 359acb3362
question: 'PerformanceWarning: DataFrame is highly fragmented when one-hot encoding
  categorical columns in a loop'
sort_order: 33
---

pandas raises `PerformanceWarning: DataFrame is highly fragmented` when you add many columns one by one, for example `df[name] = (df[col] == value).astype(int)` inside nested loops. Each insert adds a separate internal block.

Don't build one-hot columns by hand. Encode all categorical columns in one call, as in Module 3:

```python
from sklearn.feature_extraction import DictVectorizer

dv = DictVectorizer(sparse=False)
train_dicts = df_train[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)
```

`pd.get_dummies(df, columns=categorical)` also works in a single call.

If you do need a loop, collect the new columns in a dict and concatenate once:

```python
new_cols = {}
for col in categorical:
    for value in df[col].unique():
        new_cols[f'{col}_{value}'] = (df[col] == value).astype(int)

df = pd.concat([df, pd.DataFrame(new_cols)], axis=1)
```
