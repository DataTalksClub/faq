---
id: 9b0e2d6a47
question: 'Project: how do I evaluate a recommender-style RAG (no obvious Q&A ground
  truth)?'
sort_order: 9
---

Two complementary approaches that both score for the evaluation criterion:

1. Synthetic ground truth (same idea as the course, adapted). For each item in your dataset, prompt the LLM with the item's description and ask it to generate ~5 user queries that should return that item as the top result. Then run those queries through your retrieval and measure hit rate / MRR / NDCG.

2. LLM-as-a-judge for end-to-end quality. Sample queries, run the full RAG, and have an LLM rate the result for relevance/usefulness on a fixed rubric (e.g. 1–5 scale, with criteria you specify in the prompt).

NDCG is often a better fit than hit-rate for ranking-style problems where multiple items are acceptable answers — it rewards getting good items high in the list, not just first.
