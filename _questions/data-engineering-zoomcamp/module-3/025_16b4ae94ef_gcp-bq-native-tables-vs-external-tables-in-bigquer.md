---
id: 16b4ae94ef
question: 'BigQuery: native tables vs external tables — what''s the difference and
  how do I create them?'
sort_order: 25
---

A native (regular) table stores data inside BigQuery's managed storage. An external table only stores metadata in BigQuery — the actual data lives in GCS (or S3, Drive). When you query an external table, BigQuery reads the underlying files at query time.

Trade-offs:

- Native: faster queries, partition/cluster support, predictable cost. Uses BigQuery storage.
- External: no data duplication, easy to add files via globs. Slower than native, fewer optimizations, query cost depends on bytes scanned in GCS.

## Create an external table from Parquet files in GCS

```sql
CREATE OR REPLACE EXTERNAL TABLE `your_project.your_dataset.yellow_taxi_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://your-bucket/yellow_tripdata_2024-*.parquet']
);
```

The `*` wildcard lets you point at every monthly file at once. Make sure all files have a compatible schema.

## Create a native table from an existing external table

```sql
CREATE OR REPLACE TABLE `your_project.your_dataset.yellow_taxi`
AS
SELECT * FROM `your_project.your_dataset.yellow_taxi_external`;
```

This materializes the data into BigQuery storage so subsequent queries are faster and cheaper.

## Can I create an external table directly from a public URL (e.g. nyc.gov)?

No — BigQuery's external table sources are limited to Cloud Storage, BigTable, and Google Drive. To use data from a public URL, download it to a GCS bucket first (manually, with `gsutil cp`, or via your ingestion pipeline), then point the external table at the bucket.

References:
- [External tables](https://cloud.google.com/bigquery/docs/external-tables)
- [Tables introduction](https://cloud.google.com/bigquery/docs/tables-intro)
