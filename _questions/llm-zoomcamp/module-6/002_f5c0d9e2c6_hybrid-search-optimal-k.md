---
id: f5c0d9e2c6
question: How to determine the optimal number of results (k) for keyword search and
  vector search when using RRF in a hybrid search?
sort_order: 2
---

Overview: In a small corpus, keep the number of retrieved results (n) relatively low to avoid noise. A good starting point is about 5–15% of the corpus per method, which translates to roughly n = 10–30.

In a hybrid setup, keyword search (more precise) should use fewer results (e.g., 10–20), while vector search (broader and semantic) performs better with slightly more (e.g., 20–30). Since RRF rewards higher-ranked items, increasing n too much provides diminishing returns and can degrade performance.

Best practice: tune these values empirically using a small evaluation set of queries with known relevant documents. Test combinations (e.g., keyword n ∈ [5,10,15,20], vector n ∈ [10,20,30]) and measure metrics to identify the best trade-off.

Practical steps:
- Define a small gold-standard query set with known relevant documents.
- Run experiments across the specified n-pairs for keyword and vector searches, computing evaluation metrics.
- Compare results and select the configuration that offers the best balance between precision/recall and retrieval quality.
- Validate the chosen configuration on additional queries if possible.

Notes: The optimal values depend on corpus size, domain, and embedding/search quality. If the corpus grows, adjust n accordingly to maintain precision without introducing excessive noise.