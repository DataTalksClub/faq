---
id: 05aad03ef3
question: 'Invalid data types after Ingesting FHV data through parquet files: Could
  not parse SR_Flag as Float64, Couldn’t parse datetime column as timestamp, couldn’t
  handle NULL values in PULocationID, DOLocationID'
sort_order: 76
---

If you uploaded the FHV 2019 parquet files manually after downloading from [this source](https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-*.parquet), you may face errors regarding data types while loading the data into a landing table (e.g., `fhv_tripdata`). To avoid these errors, create an external table with the schema defined as follows and load each month in a loop:

```sql
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
```

You can also use:

```sql
uris = ['gs://project id/fhv_2019_*.parquet']
```

This approach removes the need for a loop and allows you to process all months in a single run.