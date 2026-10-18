---
id: 2d5fc21aff
question: 'Homework 3 Q4: Why does `round(accuracy, 2)` give me a value that doesn’t
  match any option?'
sort_order: 31
---

This mismatch is usually caused by rounding a `numpy.float64` instead of a regular Python `float`.

- `(y_pred == y_val).mean()` returns a NumPy scalar (`np.float64`). NumPy’s `round`/rounding behavior can differ from Python’s `round` because of how they handle half-way cases.
- The homework reference solution computes accuracy with `accuracy_score`, which returns a Python `float`, making rounding match the expected options.

Fixes:

1) Convert to a Python `float` before rounding:

```python
round(float((y_pred == y_val).mean()), 2)
```

2) Or compute accuracy with scikit-learn:

```python
from sklearn.metrics import accuracy_score

round(accuracy_score(y_val, y_pred), 2)
```

If you still don’t match options, double-check you’re using the pinned dataset/reproducible split as required by the homework, but the `np.float64` vs `float` difference is the core cause of this particular rounding discrepancy.