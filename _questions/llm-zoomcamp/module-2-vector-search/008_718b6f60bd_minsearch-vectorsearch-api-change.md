---
id: 718b6f60bd
question: Why doesn't the VectorSearch example from the lesson work with the latest
  version of minsearch, and how should I build the vector index now?
sort_order: 8
---

The VectorSearch API has changed in recent versions of minsearch. The older pattern of passing embedding_model to the constructor is no longer supported. Instead, you generate embeddings first, then build the index with those embeddings and their associated payloads. The recommended workflow is:

1. Generate embeddings for all document chunks.
2. Create a VectorSearch instance.
3. Build the index using fit(vectors, payload).
4. Encode the query.
5. Search using the query vector.

Example:

```python
from minsearch import VectorSearch

vindex = VectorSearch(
    keyword_fields=["filename"]
)

vindex.fit(
    vectors=X,
    payload=chunks
)

query_vector = embedder.encode(query)

results = vindex.search(
    query_vector,
    num_results=5
)
```

Notes:
- If you encounter the error shown in the lesson, check which version of minsearch you have installed and refer to the current API documentation, since the constructor may no longer accept embedding_model and embeddings may need to be generated prior to indexing.