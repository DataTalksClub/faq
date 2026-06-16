---
id: 92cd22cada
question: Why was .dot(...) used directly to compute cosine similarity in the lesson,
  but normalization is emphasized in the homework?
sort_order: 3
---

In the lesson, `.dot(...)` was used under the assumption that the embeddings returned by the model (e.g., `model.encode(...)` from OpenAI) are already normalized to have unit length. In that case, the dot product is mathematically equivalent to cosine similarity.

In the homework, however, we use classic embeddings like TF-IDF + SVD, which are not normalized by default. This means that the dot product does not represent cosine similarity unless we manually normalize the vectors.