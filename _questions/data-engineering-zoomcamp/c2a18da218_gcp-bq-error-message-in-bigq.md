---
course: data-engineering-zoomcamp
id: c2a18da218
question: 'GCP BQ - Error Message in BigQuery: annotated as a valid Timestamp, please
  annotate it as TimestampType(MICROS) or TimestampType(MILLIS)'
section: 'Module 3: Data Warehousing'
sort_order: 2110
---

Background:

`pd.read_parquet`

`pd.to_datetime`

`pq.write_to_dataset`

Reference:

Solution:

Add `use_deprecated_int96_timestamps=True` to `pq.write_to_dataset` function, like below

pq.write_to_dataset(

table,

root_path=root_path,

filesystem=gcs,

use_deprecated_int96_timestamps=True

# Write timestamps to INT96 Parquet format

)

