---
id: 46d95787b3
question: When should partitioning be used instead of clustering, and vice versa?
sort_order: 47
---

- Partitioning is most effective when queries consistently filter by a time-based column such as a date or timestamp.
- Clustering is most useful when queries frequently filter or sort on low-cardinality columns like IDs.
- They are complementary techniques and are often used together when access patterns justify it.