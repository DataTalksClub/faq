---
id: e2d595f23c
question: Why is the number of documents in the FAQ dataset different from the video, and why do my RAG results differ?
sort_order: 19
---

The course loads documents from the live FAQ dataset, which changes over time as
questions are added, updated, or deleted. If your notebook downloads the latest
data, its document count and RAG index can differ from the snapshot used when the
videos were recorded. Different retrieved context can then produce a different
final answer.

This does not necessarily mean your implementation is wrong. To reproduce a
video exactly, use the same dataset snapshot or Git commit; otherwise, expect
results from the current dataset to differ.
