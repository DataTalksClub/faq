---
course: data-engineering-zoomcamp
id: 05aad03ef3
question: 'Invalid data types after Ingesting FHV data through parquet files: Could
  not parse SR_Flag as Float64,Couldn’t parse datetime column as timestamp,couldn’t
  handle NULL values in PULocationID,DOLocationID'
section: 'Module 4: analytics engineering with dbt'
sort_order: 3160
---

If you uploaded manually the fvh 2019 parquet files manually after downloading from  you may face errors regarding date types while loading the data in a landing table (say fhv_tripdata). Try to create an the external table with the schema defines as following and load each month in a loop.

-----Correct load with schema defination----will not throw error----------------------

CREATE OR REPLACE EXTERNAL TABLE `dw-bigquery-week-3.trips_data_all.external_tlc_fhv_trips_2019` (

dispatching_base_num STRING,

pickup_datetime TIMESTAMP,

dropoff_datetime TIMESTAMP,

PUlocationID FLOAT64,

DOlocationID FLOAT64,

SR_Flag FLOAT64,

Affiliated_base_number STRING

)

OPTIONS (

format = 'PARQUET',

uris = ['gs://project id/fhv_2019_8.parquet']

);

Can Also USE  uris = ['gs://project id/fhv_2019_*.parquet'] (THIS WILL remove the need for the loop and can be done for all month in single RUN )

– THANKYOU FOR THIS –

