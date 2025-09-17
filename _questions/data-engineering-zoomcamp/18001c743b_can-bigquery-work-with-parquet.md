---
course: data-engineering-zoomcamp
id: 18001c743b
question: Can BigQuery work with parquet files directly?
section: 'Module 3: Data Warehousing'
sort_order: 2310
---

Yes, you can load your Parquet files directly into your GCP (Google Cloud Platform) Bucket first, then via BigQuery, you can create an external table of these Parquet files with a query statement like this:

CREATE OR REPLACE EXTERNAL TABLE `module-3-data-warehouse.taxi_data.external_yellow_tripdata_2024`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://module3-dez/yellow_tripdata_2024-*.parquet']
);

Make sure to adjust the sql statement to your own situation and directories.
The * symbol can be used as a wildcard, which you will need to target Parquet files of all the months of 2024.

