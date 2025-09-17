---
course: data-engineering-zoomcamp
id: c36b3f5196
question: GCP BQ - External and regular table
section: 'Module 3: Data Warehousing'
sort_order: 2300
---

External Table (data remains in GCS bucket)

Regular Table (data is copied into BigQuery storage)

Example of creating external table:

CREATE OR REPLACE EXTERNAL TABLE `your_project.your_dataset.tablenamel`

OPTIONS (

format = 'PARQUET',

uris = ['gs://your-bucket-name/yellow_tripdata_2024-*.parquet']

);

Example of creating regular table from extermal table

CREATE OR REPLACE TABLE `your_project.your_dataset.tablename`

AS

SELECT * FROM `your_project.your_dataset.yellow_taxi_external`;

Or directly load data form GCS into a regular BigQuery table without creating an external table using:

CREATE OR REPLACE TABLE `your_project.your_dataset.yellow_taxi_table`

OPTIONS (

format = 'PARQUET'

) AS

SELECT * FROM `your_project.your_dataset.external_table_placeholder`

FROM EXTERNAL_QUERY(

'your_project.region-us.gcs_external',

'SELECT * FROM `gs://your-bucket-name/yellow_tripdata_2024-*.parquet`'

);

