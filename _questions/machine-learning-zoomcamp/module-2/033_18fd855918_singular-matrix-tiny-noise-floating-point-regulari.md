---
id: 18fd855918
question: 'LinAlgError: Singular matrix when adding tiny noise (e.g., 5.00000001)
  to duplicated columns—floating-point precision issue?'
sort_order: 33
---

In that part of the lesson, adding a tiny bit of noise (like `5.00000001`) is meant to make nearly-duplicate columns “slightly different”, so the normal-equation Gram matrix becomes invertible and you get huge weights.

If you instead see `LinAlgError: Singular matrix`, it’s usually because of floating-point precision differences between your environment and the one used in the video. The noise you add may be so small (e.g., difference on the order of `1e-8`) that after forming `X.T @ X`, the rounding in `X.T @ X` can make the matrix effectively singular. Different `numpy` versions and linear algebra backends (OpenBLAS/MKL/Apple Accelerate) can change whether the result is treated as singular.

That’s also why later in the lesson a slightly larger noise (e.g., `1.0000001`) may work: the perturbation survives rounding better.

How to validate the lesson behavior
- Try a slightly larger noise than `5.00000001` in your duplicated column and recompute `XTX = X.T @ X`.

Fix
- Apply regularization (the lesson’s goal): add a small value to the diagonal before inverting.

Example:
```python
XTX = X.T @ X
XTX = XTX + 0.01 * np.eye(XTX.shape[0])
W = np.linalg.inv(XTX) @ X.T @ y
```
Use `np.eye(XTX.shape[0])` (or otherwise match the feature dimension) rather than hard-coding `np.eye(3)` so it works for the right number of features.