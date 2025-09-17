---
id: 8c9b0fdaa5
question: Invalid date types after Ingesting FHV data through CSV files: Could not parse 'pickup_datetime' as a timestamp
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3150
---

If you uploaded manually the fvh 2019 csv files, you may face errors regarding date types. Try to create an the external table in bigquery but define the pickup_datetime and dropoff_datetime to be strings

CREATE OR REPLACE EXTERNAL TABLE `gcp_project.trips_data_all.fhv_tripdata`  (

dispatching_base_num STRING,

pickup_datetime STRING,

dropoff_datetime STRING,

PUlocationID STRING,

DOlocationID STRING,

SR_Flag STRING,

Affiliated_base_number STRING

)

OPTIONS (

format = 'csv',

uris = ['gs://bucket/*.csv']

);

Then when creating the fhv core model in dbt, use TIMESTAMP(CAST(()) to ensure it first parses as a string and then convert it to timestamp.

with fhv_tripdata as (

select * from {{ ref('stg_fhv_tripdata') }}

),

dim_zones as (

select * from {{ ref('dim_zones') }}

where borough != 'Unknown'

)

select fhv_tripdata.dispatching_base_num,

TIMESTAMP(CAST(fhv_tripdata.pickup_datetime AS STRING)) AS pickup_datetime,

TIMESTAMP(CAST(fhv_tripdata.dropoff_datetime AS STRING)) AS dropoff_datetime,

