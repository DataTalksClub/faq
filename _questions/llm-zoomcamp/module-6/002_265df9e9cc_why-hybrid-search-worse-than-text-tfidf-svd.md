---
id: 265df9e9cc
question: Why did my hybrid (text + vector) search score worse than text search alone
  (e.g., TF-IDF+SVD on the vector side)?
sort_order: 2
---

If the “vector” side is `TF-IDF+SVD` (or another representation derived from the same word-frequency signal) rather than a real embedding model, then it may not provide an independent notion of meaning.

When you average two correlated scores (50/50), the weaker/blurrier signal can dilute the stronger text signal—so documents that were ranked correctly by text-only can be pushed down once hybrid combines scores.

Before concluding that hybrid search is inherently broken:

1. Evaluate all three methods separately on the same ground-truth questions:

```python
text_hit_rate = evaluate(text_search, ground_truth)
vector_hit_rate = evaluate(vector_search, ground_truth)
hybrid_hit_rate = evaluate(hybrid_search, ground_truth)
```

2. If `vector_hit_rate` is close to `text_hit_rate` (i.e., the signals are too similar) or `vector_hit_rate` is clearly worse, then your two inputs aren’t complementing each other—hybrid is likely underperforming because it’s averaging down the better signal.

A fix is to use a genuinely independent semantic signal from a real embedding model (e.g., sentence-transformers like `all-MiniLM-L6-v2`), so hybrid has two different ways to match meaning rather than one strong signal diluted by a correlated copy.

Source: https://www.sbert.net/