---
id: d9072c7279
question: Inconsistent number of rows when re-running fact_trips model
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2900
---

This is due to the way the deduplication is done in the two staging files.

Solution: add order by in the partition by part of both staging files. Keep adding columns to order by until the number of rows in the fact_trips table is consistent when re-running the fact_trips model.

Explanation (a bit convoluted, feel free to clarify, correct etc.)

We partition by vendor id and pickup_datetime and choose the first row (rn=1) from all these partitions. These partitions are not ordered, so every time we run this, the first row might be a different one. Since the first row is different between runs, it might or might not contain an unknown borough. Then, in the fact_trips model we will discard a different number of rows when we discard all values with an unknown borough.

