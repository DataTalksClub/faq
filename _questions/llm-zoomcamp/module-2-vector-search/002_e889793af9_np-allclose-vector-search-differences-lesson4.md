---
id: e889793af9
question: Why can np.allclose(scores, scores_loop) return False when comparing the
  matrix multiplication version of vector search with a Python for loop? Aren't they
  doing the same math?
sort_order: 2
---

In Lesson 4: Vector Search, the matrix version uses optimized low-level numerical code (e.g., BLAS) for the dot product results, while a Python loop accumulates sums sequentially. Although the math is the same, floating-point precision and the order of summation can produce tiny differences in the final values. Depending on the exact data and vectors in the index, these small differences can cause np.allclose to pass or fail if the tolerance is too strict.

To make the comparison more robust against minor numerical differences, you can allow a small absolute tolerance with allclose, for example:

```python
print(f"Loop matches matrix version: {np.allclose(scores, scores_loop, atol=1e-5)}")
```

With that adjustment, the comparison should be more robust across small numerical differences.