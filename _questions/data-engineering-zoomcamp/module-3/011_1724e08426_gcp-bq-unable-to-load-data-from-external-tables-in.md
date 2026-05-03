---
id: 1724e08426
question: 'GCP BQ: Unable to load data from external tables into a materialized table
  in BigQuery due to an invalid timestamp error that are added while appending data
  to the file in Google Cloud Storage'
sort_order: 11
---

```plaintext
could not parse 'pickup_datetime' as timestamp for field pickup_datetime (position 2)
```

This error is caused by invalid data in the timestamp column. To resolve this issue:

1. Define the schema of the external table using the `STRING` datatype for the timestamp column. This allows queries to execute without errors.
2. Filter out the invalid timestamp rows during data import.
3. Insert the filtered rows into the materialized table, specifying the `TIMESTAMP` datatype for the timestamp fields.