---
id: 2c24ec504d
question: Why are my RAG results different from the results shown in the lecture?
sort_order: 34
---

The course dataset is updated over time. If your notebook downloads the latest
course documents, your index may contain different content from the snapshot
used when the lecture was recorded. That changes the retrieved context and
therefore the final answer.

This does not necessarily mean your RAG implementation is wrong. To reproduce
the lecture exactly, use the same dataset snapshot or Git commit. Otherwise,
use the current dataset and expect the results to differ.
