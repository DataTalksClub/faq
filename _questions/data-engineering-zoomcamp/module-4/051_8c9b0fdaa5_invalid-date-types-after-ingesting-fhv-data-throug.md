---
id: 8c9b0fdaa5
question: 'Schema and type errors when ingesting FHV data (timestamps fail to parse,
  Parquet column type mismatches, NULL handling)'
sort_order: 51
---

The FHV 2019 dataset has multiple schema gotchas. The fix depends on which file format you ingested.

## CSV: timestamps fail to parse

```
Could not parse 'pickup_datetime' as a timestamp
```

Define the timestamp columns as `STRING` in the external table, then cast them in the staging model. This avoids BigQuery rejecting rows with malformed timestamps at load time:

```sql
CREATE OR REPLACE EXTERNAL TABLE `gcp_project.trips_data_all.fhv_tripdata` (
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

In your staging model, cast through `TIMESTAMP(CAST(... AS STRING))`:

```sql
SELECT
  TIMESTAMP(CAST(pickup_datetime AS STRING)) AS pickup_datetime,
  TIMESTAMP(CAST(dropoff_datetime AS STRING)) AS dropoff_datetime,
  ...
FROM {{ ref('stg_fhv_tripdata') }}
```

To skip type-detection issues entirely, you can also load with `bq load --autodetect --allow_quoted_newlines --source_format=CSV` from a `.csv.gz` file in GCS — see the BigQuery CLI external-table FAQ.

## Parquet: column type mismatch (FLOAT vs INT) or NULL location IDs

```
Parquet column 'PULocationID' has type INT64 which does not match the target cpp_type DOUBLE
Could not parse SR_Flag as Float64
```

Pandas reads integer columns with NULL values as floats by default, which produces a Parquet file with `DOUBLE` columns. BigQuery's external table then conflicts with your declared schema.

Two options:

a) Define the external table schema with `FLOAT64` for the offending location ID columns (matches what Parquet actually has):

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
  uris = ['gs://project/fhv_2019_*.parquet']
);
```

b) Fix the Parquet at write time by using pandas' nullable `Int64`:

```python
df['PUlocationID'] = df['PUlocationID'].astype('Int64')
df['DOlocationID'] = df['DOlocationID'].astype('Int64')
```

Or coerce the whole DataFrame:

```python
df.fillna(-999999, inplace=True)
df = df.convert_dtypes()
df = df.replace(-999999, None)
```

This produces a Parquet file with the right INT64 schema and avoids the issue downstream.

## When the column types differ between months

Some FHV month files have `PUlocationID` as INT, others as FLOAT, leading to:

```
error: Error while reading data: Parquet column 'PUlocationID' has type INT which does not match the target cpp_type DOUBLE
```

The first file BigQuery loads defines the table schema, and subsequent files with a different schema fail. Force consistent types when generating the Parquet (option b above) or load the months that have the same schema in groups.

## "Bad int64 value" on cast in the dbt model

For `ehail_fee`, `ratecodeid`, `trip_type`, etc. — see the dedicated bad-int64 / parquet-schema FAQ.
