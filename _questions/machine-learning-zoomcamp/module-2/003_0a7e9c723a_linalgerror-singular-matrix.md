---
id: 0a7e9c723a
question: 'np.linalg.inv(XTX) throws LinAlgError: Singular matrix — what does this
  mean?'
sort_order: 3
---

A `LinAlgError: Singular matrix` from `np.linalg.inv(XTX)` means `XTX` is not invertible—typically because its rows/columns are linearly dependent (often due to redundant features or insufficient independent information).

To diagnose, check whether the matrix is rank-deficient:

- Compute `np.linalg.matrix_rank(XTX)` and compare it to the number of columns of `XTX` (if the rank is smaller, it’s singular).

Common fixes:

- Drop or combine redundant features so you get a full-rank `XTX`.
- Instead of the exact inverse, use the pseudo-inverse: `np.linalg.pinv(XTX)`. The pseudo-inverse works even when the matrix is singular, and is often the preferred approach in ML when you can’t guarantee full rank.

If you still get the error, also verify you’re forming `XTX` correctly (e.g., for linear regression it should be based on `X.T @ X`, not `X @ X.T`).