---
id: e2d595f23c
question: Why does the FAQ documents dataset have a different number of documents
  across modules (e.g. 1350 vs 1208)? Should I be concerned?
sort_order: 19
---

No, this is expected and nothing to worry about. The `documents.json` file is a snapshot of the live DataTalksClub FAQ, which keeps growing as new questions are added. Two things cause the counts to differ between lessons:

- **Different sources.** Module 1 loads the dataset from `https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json`, while the Module 2 (vector search) notebooks load it from `https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json`. These are two separate copies that were exported at different times.
- **Snapshots taken at different times.** Because the FAQ grows over time, an older export simply has fewer documents than a newer one.

The exact document count does not affect what you learn or whether your code is correct. The only time it matters is if a homework question explicitly asks for a number that depends on the dataset (e.g. "how many documents are returned") — in that case, use the dataset URL given in that specific homework so your answer matches the expected one.
