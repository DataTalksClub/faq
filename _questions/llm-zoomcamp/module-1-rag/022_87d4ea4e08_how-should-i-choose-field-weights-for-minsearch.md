---
id: 87d4ea4e08
question: How should I choose field weights for minsearch or another search engine?
sort_order: 22
---

The systematic approach is to evaluate different weight settings against a ground-truth dataset.

For example:

1. Create a small set of representative questions.
2. Mark which documents should be retrieved for each question.
3. Try different field weights.
4. Compare retrieval metrics such as hit rate, precision@k, recall@k, or MRR.

You can tune weights by trial and error for small projects, but evaluation is the more reliable approach. The course covers this topic more directly in the evaluation module.
