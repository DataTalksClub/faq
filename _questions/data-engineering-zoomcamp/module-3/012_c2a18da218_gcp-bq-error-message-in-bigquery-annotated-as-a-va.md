---
id: c2a18da218
question: 'GCP BQ: Error Message in BigQuery: annotated as a valid Timestamp, please
  annotate it as TimestampType(MICROS) or TimestampType(MILLIS)'
sort_order: 12
---

When you encounter this BigQuery error, it typically relates to how timestamps are stored in Parquet files.

### Solution:

To resolve this issue, you can modify the Parquet writing configuration by adding `use_deprecated_int96_timestamps=True` to the `pq.write_to_dataset` function. This setting writes timestamps in the INT96 format, which can be more compatible with BigQuery.

Here’s how you can adjust the function:

```python
pq.write_to_dataset(
    table,
    root_path=root_path,
    filesystem=gcs,
    use_deprecated_int96_timestamps=True  # Write timestamps to INT96 Parquet format
)
```

### References

- [Stack Overflow - Parquet compatibility with PyArrow vs PySpark](https://stackoverflow.com/questions/48314880/are-parquet-file-created-with-pyarrow-vs-pyspark-compatible)
- [Stack Overflow - Editing Parquet files and datetime format errors](https://stackoverflow.com/questions/57798479/editing-parquet-files-with-python-causes-errors-to-datetime-format)
- [Reddit - Parquet Timestamp to BQ issues](https://www.reddit.com/r/bigquery/comments/16aoq0u/parquet_timestamp_to_bq_coming_across_as_int/?share_id=YXqCs5Jl6hQcw-kg6-VgF&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1)

Use the above configuration to ensure compatibility with Google BigQuery when dealing with timestamps in Parquet files.