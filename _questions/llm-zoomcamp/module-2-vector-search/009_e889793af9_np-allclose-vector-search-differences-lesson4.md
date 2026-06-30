---
id: e889793af9
question: Why do the matrix and for-loop versions of vector search give slightly different
  results?
sort_order: 9
---

In [Lesson 4 (Vector Search)](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/lessons/04-vector-search.md) we compute the scores two ways — `scores = X.dot(v_query)` and the equivalent for-loop — and they can come out slightly different. This is normal, it's just floating-point precision. If you compare them with `np.allclose(scores, scores_loop)` you might get `False`, even though both compute the same dot products. They just add the numbers up in a slightly different order, and floating-point addition isn't perfectly associative, so the results can differ in the last few decimal places.

Under the hood, `X.dot(v)` runs optimized BLAS code that sums in a different order than a sequential Python loop. The math is the same; only the rounding differs, so the values aren't really "wrong."

Just compare them with a small tolerance instead of expecting an exact match:

```python
np.allclose(scores, scores_loop, atol=1e-5)
```
