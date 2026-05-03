---
id: 52e74f0053
question: Why are there unexpected years in lpep_pickup_datetime after loading taxi
  data into BigQuery?
sort_order: 44
---

Unexpected years in lpep_pickup_datetime after loading taxi data into BigQuery usually indicate a corrupted or incorrect load. Common causes include:

- CSV schema autodetect misinterpreting timestamp format
- Mixing Parquet and CSV loads into the same table
- Appending instead of replacing during reload
- Partial failed loads

How to verify:

- Run a range check:

```sql
SELECT
  MIN(lpep_pickup_datetime),
  MAX(lpep_pickup_datetime)
FROM `project.dataset.table`;
```

If the values fall outside the expected years (for example 2019–2020), reload the table from a clean source using a replacement load, preferably Parquet:

```bash
bq load \
  --source_format=PARQUET \
  --replace \
  dataset.table \
  gs://bucket/path/*.parquet
```

Note: Using Parquet instead of CSV often helps prevent schema interpretation issues and ensures a cleaner, replace-based reload.