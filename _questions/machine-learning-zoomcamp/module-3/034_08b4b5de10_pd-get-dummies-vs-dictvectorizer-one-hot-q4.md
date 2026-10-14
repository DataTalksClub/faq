---
id: 08b4b5de10
question: Can I use `pd.get_dummies` instead of `DictVectorizer` for one-hot encoding
  (Homework 3 Q4)?
sort_order: 34
---

Yes, you can use `pd.get_dummies`, but `DictVectorizer` is safer and is what the lectures use.

The main risk with `pd.get_dummies` is that it is applied separately to each split. If a category appears in training but not in validation (or vice versa), the encoded feature matrices can end up with a different set of columns. That can either crash your pipeline or, worse, silently misalign features.

With `DictVectorizer`, you fit on training only and then transform validation/test with the same learned mapping, so the column layout is locked. Categories not seen during `fit` are ignored, so that row gets zeros in all one-hot columns of that feature.

If you use `get_dummies`, align validation/test to the training columns:

```python
X_train = pd.get_dummies(df_train[features])
X_val = pd.get_dummies(df_val[features])
X_val = X_val.reindex(columns=X_train.columns, fill_value=0)
```
