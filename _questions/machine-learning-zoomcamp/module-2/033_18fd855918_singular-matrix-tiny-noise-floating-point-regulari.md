---
id: 18fd855918
question: 'Lesson 2.13: adding tiny noise (5.00000001) still gives LinAlgError: Singular
  matrix instead of huge weights. Why?'
sort_order: 33
---

This is a floating-point precision difference between your environment and the one used in the video, not a mistake in your code.

In the lesson, `5.00000001` makes the duplicated columns slightly different, so the instructor's NumPy finds an inverse with huge values. But the difference is so small (1e-8) that after computing `X.T @ X`, it can get lost in rounding. Depending on your NumPy version and linear algebra backend (OpenBLAS, MKL, Apple Accelerate), the matrix may be treated as exactly singular, so `np.linalg.inv` raises `LinAlgError`.

The smaller 3x3 example later in the lesson uses `1.0000001`, which survives rounding, so it still inverts.

To see the behaviour shown in the video, use a slightly larger noise value:

```python
import numpy as np

X = np.array([
    [4, 4, 4],
    [3, 5, 5],
    [5, 1, 1],
    [5, 4, 4],
    [7, 5, 5],
    [4, 5, 5.0000001],   # one more decimal place of noise
])
XTX = X.T @ X
np.linalg.inv(XTX)       # huge values, around 1e13
```

To fix it, apply regularization, which is the point of the lesson. Add a small number to the diagonal before inverting:

```python
XTX = XTX + 0.01 * np.eye(XTX.shape[0])
np.linalg.inv(XTX)       # works; values are now under control
```

This works with `5.00000001` too. Use `np.eye(XTX.shape[0])` rather than hard-coding `np.eye(3)` so it matches the number of features.

For singular matrix errors in general (duplicate features, wrong multiplication order), see "np.linalg.inv(XTX) throws LinAlgError: Singular matrix — what does this mean?".
