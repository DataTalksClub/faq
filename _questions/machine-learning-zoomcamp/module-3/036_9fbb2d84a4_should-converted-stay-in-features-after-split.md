---
id: 9fbb2d84a4
question: Should the target `converted` stay in the feature dataframe after train/val/test
  split?
sort_order: 36
---

No. Move `converted` out to `y_train`, `y_val`, and `y_test` first, then delete it from the feature dataframes:

```python
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train['converted'].values
y_val = df_val['converted'].values
y_test = df_test['converted'].values

del df_train['converted']
del df_val['converted']
del df_test['converted']
```

If the target stays in the features, the model just reads the answer from it: validation accuracy looks near-perfect, but the model is useless on new data where the target isn't known.
