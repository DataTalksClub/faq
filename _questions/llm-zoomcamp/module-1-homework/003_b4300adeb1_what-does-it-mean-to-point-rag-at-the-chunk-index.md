---
id: b4300adeb1
question: What does it mean to point RAG at the chunk index in Module 1 homework?
sort_order: 3
---

It means you should build and search the index using the chunked documents, not the original full documents.

For example, if your original records are in `documents` and your split records are in `chunks`, fit the search index on `chunks`:

```python
index.fit(chunks)
```

not:

```python
index.fit(documents)
```

Then the RAG pipeline retrieves relevant chunks and puts only those chunks into the prompt. This is what reduces the amount of context sent to the model.
