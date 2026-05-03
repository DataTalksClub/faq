---
id: 66d3c42dd4
question: 'GCP BQ: How to handle type error from BigQuery and Parquet data?'
sort_order: 19
---

When injecting data into GCS using Pandas, some datasets might have missing values in the `DOlocationID` and `PUlocationID` columns. By default, Pandas will cast these columns as `float`, leading to inconsistent data types between the Parquet files in GCS and the schema defined in BigQuery. You might encounter the following error:

```bash
error: Error while reading table: trips_data_all.external_fhv_tripdata, error message: Parquet column 'DOlocationID' has type INT64 which does not match the target cpp_type DOUBLE.
```

### Solution:
Fix the data type issue in the data pipeline:

1. Before injecting data into GCS, use `astype` and `Int64` (which is different from `int64` and accepts both missing values and integers) to cast the columns.

    Example:
    ```python
    df["PUlocationID"] = df.PUlocationID.astype("Int64")
    df["DOlocationID"] = df.DOlocationID.astype("Int64")
    ```

2. It is best to define the data type of all the columns in the Transformation section of the ETL pipeline before loading to BigQuery.