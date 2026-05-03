---
id: a83247e572
question: 'BigQuery: Datetime columns in Parquet files created from Pandas show up
  as integer columns in BigQuery'
sort_order: 13
---

When writing Parquet files from a Pandas DataFrame, Pandas may emit timestamp columns as integers (epoch milliseconds) by default. When BigQuery loads those files it sees raw `INT64` values and won't auto-promote them to `TIMESTAMP`.

Solution 1: Coerce timestamps when writing the Parquet file

Use PyArrow with `coerce_timestamps='us'` so the file carries proper `TIMESTAMP(MICROS)` logical types:

```python
import pyarrow as pa
import pyarrow.parquet as pq

table = pa.Table.from_pandas(df, preserve_index=False)

pq.write_table(
    table,
    'gs://<bucket>/<path>.parquet',
    # Force TIMESTAMP(MICROS) so BigQuery loads the column as TIMESTAMP
    coerce_timestamps='us',
    filesystem=pa.fs.GcsFileSystem(),
)
```

Solution 2: Provide an explicit schema

If you want full control over column types, pass an explicit PyArrow schema instead of relying on inference:

```python
schema = pa.schema([
    ('vendor_id', pa.int64()),
    ('lpep_pickup_datetime', pa.timestamp('us')),
    ('lpep_dropoff_datetime', pa.timestamp('us')),
    # ...
])

table = pa.Table.from_pandas(df, schema=schema)
```

Either approach also works inside an orchestrator's data-export task — adapt the `pq.write_table` call to fit your task's signature.
