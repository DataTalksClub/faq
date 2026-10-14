---
id: 0a7e9c723a
question: 'np.linalg.inv(XTX) throws LinAlgError: Singular matrix — what does this
  mean?'
sort_order: 3
---

`np.linalg.inv` raises `LinAlgError: Singular matrix` when `XTX` is not invertible, which happens when some columns of `X` are linearly dependent (duplicated or redundant features).

It's normal to hit this while following the Module 2 videos. The regularization lesson fixes it by adding a small value to the diagonal before inverting:

```python
XTX = X.T @ X
XTX = XTX + r * np.eye(XTX.shape[0])
w_full = np.linalg.inv(XTX) @ X.T @ y
```

To diagnose it, compare `np.linalg.matrix_rank(XTX)` with `XTX.shape[0]`. A smaller rank means redundant columns that you can drop or combine. `np.linalg.pinv` avoids the error, but for homework use `inv` with regularization as in the lessons, because the answer options were computed that way.

Also check that you compute `X.T @ X` (not `X @ X.T`) and that you don't invert the matrix twice.
