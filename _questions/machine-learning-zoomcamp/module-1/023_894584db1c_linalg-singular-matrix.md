---
id: 894584db1c
question: 'Homework 1: ''LinAlgError: Singular matrix'' when computing np.linalg.inv(X.T @ X)'
sort_order: 23
---

The matrix multiplication order matters. `XTX` should be `X.T @ X` (a small `n_features x n_features` matrix), NOT `X @ X.T` (an `n_samples x n_samples` matrix that's singular when columns are linearly dependent):

```python
XTX = X.T @ X        # correct, e.g. shape (2, 2)
# XTX = X @ X.T      # WRONG, e.g. shape (7, 7) and singular
```

Also confirm you reduced X to the correct rows/columns before the multiplication (e.g., for the Asia/origin filter problems: `df[df.origin == 'Asia']` first, then select columns, `.head(7)`, then `.values` / `.to_numpy()`).
