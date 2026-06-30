---
id: e2d595f23c
question: Why does the FAQ documents dataset have a different number of documents
  across modules (e.g. 1350 vs 1208)? Should I be concerned?
sort_order: 19
---

No, this is expected and nothing to worry about. Both modules use the same FAQ dataset — it's the DataTalksClub course FAQ exported to a `documents.json` file. The reason the counts differ (e.g. 1350 vs 1208) is simply that the dataset is regenerated from the FAQ over time, and the FAQ keeps growing as new questions are added. A lesson recorded later just happens to capture a larger snapshot than an earlier one.

The exact document count does not affect what you learn or whether your code is correct. The only time it matters is if a homework question explicitly asks for a number that depends on the dataset (e.g. "how many documents are returned") — in that case, use the dataset URL given in that specific homework so your answer matches the expected one.
