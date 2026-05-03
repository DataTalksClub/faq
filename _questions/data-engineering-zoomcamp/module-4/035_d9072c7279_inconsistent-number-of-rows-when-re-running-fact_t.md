---
id: d9072c7279
question: Inconsistent number of rows when re-running fact_trips model
sort_order: 35
---

This issue arises from the way deduplication is handled in two staging files.

**Solution:**

- Add an `ORDER BY` clause in the `PARTITION BY` section of both staging files.
- Continue adding columns to the `ORDER BY` clause until the row count in the `fact_trips` table is consistent upon re-running the model.

**Explanation:**

We partition by `vendor_id` and `pickup_datetime`, selecting the first row (`rn=1`) from these partitions. These partitions lack an order, so every execution might yield a different first row. The inconsistency leads to different rows being processed, possibly with or without an unknown borough. Consequently, the `fact_trips` model discards a varying number of rows based on the presence of unknown boroughs.