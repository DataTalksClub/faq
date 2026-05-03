---
id: 7df3102580
question: How to obtain the DDL of a table in BigQuery?
sort_order: 22
---

### Goal
To reproduce a BigQuery table's schema and data layout, you can query the INFORMATION_SCHEMA.TABLES to retrieve the DDL needed to recreate the table.

**For a normal (native) table in a dataset**

```sql
SELECT table_name, ddl
FROM zoomcamp.INFORMATION_SCHEMA.TABLES
WHERE table_name = 'yellow_tripdata_parquet';
```

The result is the `CREATE TABLE` statement needed to recreate the table, e.g.:

```sql
CREATE TABLE `zoomcamp-ingenieria-datos.zoomcamp.yellow_tripdata_parquet`
(
    VendorID INT64,
    tpep_pickup_datetime TIMESTAMP,
    tpep_dropoff_datetime TIMESTAMP,
    passenger_count INT64,
    trip_distance FLOAT64,
    RatecodeID INT64,
    store_and_fwd_flag STRING,
    PULocationID INT64,
    DOLocationID INT64,
    payment_type INT64,
    fare_amount FLOAT64,
    extra FLOAT64,
    mta_tax FLOAT64,
    tip_amount FLOAT64,
    tolls_amount FLOAT64,
    improvement_surcharge FLOAT64,
    total_amount FLOAT64,
    congestion_surcharge FLOAT64,
    Airport_fee FLOAT64
);
```

**For an external table**

```sql
SELECT table_name, ddl
FROM zoomcamp.INFORMATION_SCHEMA.TABLES
WHERE table_name = 'yellow_tripdata_parquet_ext';
```

The result would contain the DDL including the path of the external files, e.g.:

```sql
CREATE EXTERNAL TABLE `zoomcamp-ingenieria-datos.zoomcamp.yellow_tripdata_parquet_ext`
OPTIONS(
    format="PARQUET",
    uris=["gs://newyork-taxi/yellow_tripdata_*.parquet"]
);
```

Notes
- This method works for both native and external tables. The exact path and URIs will depend on your dataset.
- For more details, see the BigQuery information_schema-tables documentation.