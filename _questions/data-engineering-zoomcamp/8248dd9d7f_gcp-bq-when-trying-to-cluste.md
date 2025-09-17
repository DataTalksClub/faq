---
course: data-engineering-zoomcamp
id: 8248dd9d7f
question: 'GCP BQ - When trying to cluster by DATE(tpep_pickup_datetime) it gives
  an error: Entries in the CLUSTER BY clause must be column names'
section: 'Module 3: Data Warehousing'
sort_order: 2230
---

No need to convert as you can cluster by a TIMESTAMP column directly in BigQuery. BigQuery supports clustering on TIMESTAMP, DATE, DATETIME, STRING, INT64, and BOOL types.

clustering sorts data based on the timestamp to optimize queries with filters like WHERE tpep_pickup_datetime BETWEEN ..., rather than creating discrete partitions.

If your goal is to improve performance for time-based queries, combining partitioning by DATE(event_time) and clustering by tpep_pickup_datetime is a good approach.

