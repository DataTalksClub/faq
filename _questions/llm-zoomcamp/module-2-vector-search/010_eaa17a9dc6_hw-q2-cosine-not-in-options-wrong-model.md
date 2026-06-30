---
id: eaa17a9dc6
question: My Module 2 homework cosine similarity (Q2) isn't any of the options — what
  am I doing wrong?
sort_order: 10
---

The most common cause is using a different embedding model than the homework specifies. Homework 2 tells you **not** to use `sentence-transformers` and to use the lightweight ONNX `Embedder` from `embedder.py` instead:

```python
from embedder import Embedder
model = Embedder()
```

Both approaches produce the same vectors for the same model, but if you embed with a different model (for example the `multi-qa-mpnet-base-dot-v1` model from the lessons, or `all-mpnet-base-v2`) you'll get a cosine value that isn't among the options.

Also check that:

- You're embedding the page's `content` field (not the filename or the whole dict).
- You're comparing against the query vector from Q1.
- The vectors are normalized — the `Embedder` returns normalized vectors, so the dot product is the cosine similarity directly.

If your value is still slightly off after using the right model, pick the closest option — small numerical differences are expected.
