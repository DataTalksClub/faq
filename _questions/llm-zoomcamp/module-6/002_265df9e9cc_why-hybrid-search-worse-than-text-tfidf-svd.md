---
id: 265df9e9cc
question: Why did my hybrid (text + vector) search score worse than text search alone?
sort_order: 2
---

If the "vector" side is TF-IDF+SVD — or anything else built from the same word-frequency signal as the text index — rather than a real embedding model, it matches on word overlap just like the text index does, so it adds nothing new. The course combines the two sides with a weighted sum (`score = alpha * vector_score + (1 - alpha) * keyword_score`) or rank fusion, so mixing a weaker, correlated signal 50/50 with a strong one dilutes the strong signal: documents ranked correctly by text-only get pushed down.

Before concluding hybrid search is broken, score text-only, vector-only, and hybrid separately on the same ground-truth questions and compare hit rates. If the vector side scores close to or worse than text-only, the two inputs are too similar (or the vector side too weak) to add anything — hybrid will underperform its stronger input rather than beat it.

The fix is to use a real embedding model such as `all-MiniLM-L6-v2` from [sentence-transformers](https://www.sbert.net/), which captures meaning rather than word overlap — see the [Module 6 hybrid search lesson](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/cohorts/2026/06-best-practices/02-hybrid-search.md).
