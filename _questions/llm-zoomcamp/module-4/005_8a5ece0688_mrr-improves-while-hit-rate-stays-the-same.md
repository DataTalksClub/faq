---
id: 8a5ece0688
question: "Why can MRR improve while Hit Rate stays the same?"
sort_order: 5
---

Hit Rate can stay unchanged while MRR improves when the same queries still
retrieve a relevant document in the top‑k results, but the first relevant
document moves higher. For example, moving a correct result from position 5 to
position 1 leaves that query's Hit Rate contribution at `1`, while its
reciprocal-rank contribution improves from `1/5` to `1`.

If the final Hit Rate and MRR values are exactly equal, verify the evaluation
code before trusting the result. Equality is legitimate only when every query
with a hit has its first relevant result at position 1 (including the special
case where both metrics are zero). Check that:

- Hit Rate counts a query once when any result is relevant.
- MRR uses only the first relevant result and calculates `1 / (rank + 1)`.
- The MRR loop stops after the first relevant result.
- Both metrics divide by the same total number of queries.
- The relevance labels and result ordering are correct before aggregation.

Reranking, chunking, or embedding changes can improve MRR without changing Hit
Rate, but inspect the per-query relevance lists to confirm that relevant results
actually moved upward.
