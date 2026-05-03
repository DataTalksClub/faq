---
id: 7be69bdcb4
question: Loading dlt exports from GCS filesystems (compressed by default)
sort_order: 11
---

When using the filesystem destination, you may have issues reading the exported files because dlt compresses them by default. If you are using `loader_file_format="parquet"` then BigQuery should cope with the compression OK. If you want to use JSONL or CSV format, however, you may need to disable file compression to avoid issues with reading the files directly in BigQuery. To do this, set the following config:

```toml
[normalize.data_writer]
disable_compression = true
```

There is further information at the [dlt docs on filesystem compression](https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#file-compression).
