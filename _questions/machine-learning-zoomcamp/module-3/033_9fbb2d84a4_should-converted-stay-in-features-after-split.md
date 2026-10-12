---
id: 9fbb2d84a4
question: Should the target `converted` stay in the feature dataframe after train/val/test
  split?
sort_order: 33
---

No—move `converted` out to `y_train`, `y_val`, and `y_test` first, then delete it from the feature dataframes.

A typical pattern is:
1) Split `df` into `df_full_train`/`df_test`, then split `df_full_train` into `df_train`/`df_val`.
2) Reset indices.
3) Extract the target into `y_train`, `y_val`, `y_test`.
4) Drop the target column from each dataframe so it’s not used as an input feature.

Example:
```python
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train[target].values
y_val = df_val[target].values
y_test = df_test[target].values

del df_train[target]
del df_val[target]
del df_test[target]
```