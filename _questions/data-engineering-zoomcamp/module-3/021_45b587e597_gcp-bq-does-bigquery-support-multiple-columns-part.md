---
id: 45b587e597
question: 'BigQuery limits: partitioning columns, clustering columns, partition counts'
sort_order: 21
---

The most commonly hit BigQuery limits in the course:

- Partition columns per table: 1. You cannot partition by multiple columns. ([docs](https://cloud.google.com/bigquery/docs/partitioned-tables#limitations))
- Cluster columns per table: up to 4. You can cluster on a tuple of columns up to that limit. ([docs](https://cloud.google.com/bigquery/docs/creating-clustered-tables#clustered_column_requirements))
- Partitions per table: 10,000 (older docs and the course playlist may say 4,000 — that limit was raised). ([docs](https://docs.cloud.google.com/bigquery/quotas#partitioned_tables))
- Partitions modified by a single job: 4,000. A single load/query/copy/DML job can't touch more than 4,000 partitions at once.

Implications for time-based partitioning under the 10,000 partition limit:

- Daily partitions cover ~27 years.
- Hourly partitions cover ~416 days (just over a year).
- Monthly partitions cover over 800 years.

So daily partitioning is fine for almost any workload; hourly partitioning needs a retention strategy if your data goes back more than ~1 year.
