---
id: 95feb4e75b
question: Why does cosine similarity reduce to a matrix multiplication between the
  embeddings and the query vector?
sort_order: 6
---

Cosine similarity measures how aligned two vectors are, regardless of their magnitude. When all vectors (including the query) are normalized to unit length, their magnitudes no longer matter. In this case, cosine similarity is equivalent to simply taking the dot product between the query and each document embedding. This allows us to compute similarities efficiently using matrix multiplication.