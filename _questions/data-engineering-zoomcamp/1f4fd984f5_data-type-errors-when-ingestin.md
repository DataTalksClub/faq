---
course: data-engineering-zoomcamp
id: 1f4fd984f5
question: Data type errors when ingesting with parquet files
section: 'Module 4: analytics engineering with dbt'
sort_order: 2890
---

The easiest way to avoid these errors is by ingesting the relevant data in a .csv.gz file type. Then, do:

CREATE OR REPLACE EXTERNAL TABLE `dtc-de.trips_data_all.fhv_tripdata`

OPTIONS (

format = 'CSV',

uris = ['gs://dtc_data_lake_dtc-de-updated/data/fhv_all/fhv_tripdata_2019-*.csv.gz']

);

As an example. You should no longer have any data type issues for week 4.

