---
id: 1a7b27c4df
question: 'Why do I get IndexError: list index out of range when accessing the best
  chunk?'
sort_order: 10
---

The error typically happens when the number of embeddings you generate does not match the number of document chunks. Make sure you create embeddings directly from the chunk list:

```python
contents = [chunk["content"] for chunk in chunks]
X = embedder.encode_batch(contents)
```

The number of rows in `X` should be equal to `len(chunks)`.
