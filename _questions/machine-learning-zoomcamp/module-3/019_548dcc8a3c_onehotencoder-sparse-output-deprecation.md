---
id: 548dcc8a3c
question: Why am I getting TypeError while creating OneHotEncoder Object?
sort_order: 19
---

In scikit-learn >= 1.2, `OneHotEncoder` no longer accepts the sparse parameter. It now uses the `sparse_output` parameter to control whether the output is sparse or dense.

What to do:
- For a dense array: use `OneHotEncoder(sparse_output=False)`.
- For a sparse matrix: use `OneHotEncoder(sparse_output=True)`.

If you previously wrote `ohe = OneHotEncoder(sparse=False)` and get a `TypeError`, replace it with `ohe = OneHotEncoder(sparse_output=False)`.

Example:

```python
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse_output=False)
X_train_cat = ohe.fit_transform(df_train[categorical_columns].values)
```

Notes:
- A dense array will be returned if `sparse_output=False`; otherwise, you’ll get a scipy sparse matrix.
- If you need a dense array from a sparse result, call `.toarray()` on the result.
- This change ensures better memory efficiency and consistency in newer scikit-learn versions.
