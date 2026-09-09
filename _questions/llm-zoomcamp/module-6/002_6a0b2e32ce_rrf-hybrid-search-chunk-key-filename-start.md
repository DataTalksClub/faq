---
id: 6a0b2e32ce
question: Why do we use `(doc['filename'], doc['start'])` as the key when combining
  hybrid search results with RRF in the LLM Zoomcamp implementation?
sort_order: 2
---

In the hybrid search implementation, you retrieve results as matching chunks from the indexed documents. Since a single source document can be split into multiple chunks, multiple results may share the same `filename` but have different `start` offsets.

Using a `(filename, start)` tuple makes the identity granular to the chunk level, so RRF combines scores for the exact same chunk when it appears in both the text-search and vector-search result lists:

```python
key = (doc["filename"], doc["start"])
```

If you used only `doc["filename"]`, then different chunks from the same document would be treated as the same item and their RRF contributions could be incorrectly merged. In short: RRF is ranking/combining chunks, not whole source files, so the key must uniquely identify a chunk. See the RRF implementation in the [Module 2 vector-search homework](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/02-vector-search/homework.md).
