---
id: 8c9b0fdaa5
question: 'Invalid date types after Ingesting FHV data through CSV files: Could not
  parse ''pickup_datetime'' as a timestamp'
sort_order: 75
---

If you uploaded manually the FHV 2019 CSV files, you may face errors regarding date types. Try to create an external table in BigQuery but define the `pickup_datetime` and `dropoff_datetime` to be strings:

```sql
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
```

Then, when creating the FHV core model in dbt, use `TIMESTAMP(CAST(())` to ensure it first parses as a string and then converts it to a timestamp:

```sql
WITH fhv_tripdata AS (
    SELECT * FROM {{ ref('stg_fhv_tripdata') }}
),
dim_zones AS (
    SELECT * FROM {{ ref('dim_zones') }}
    WHERE borough != 'Unknown'
)
SELECT fhv_tripdata.dispatching_base_num,
    TIMESTAMP(CAST(fhv_tripdata.pickup_datetime AS STRING)) AS pickup_datetime,
    TIMESTAMP(CAST(fhv_tripdata.dropoff_datetime AS STRING)) AS dropoff_datetime,
```