---
id: 66d3c42dd4
question: GCP BQ - How to handle type error from big query and parquet data?
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2190
---

Problem: When you inject data into GCS using Pandas, there is a chance that some dataset has missing values on  DOlocationID and PUlocationID. Pandas by default will cast these columns as float data type, causing inconsistent data type between parquet in GCS and schema defined in big query. You will see something like this:

error: Error while reading table: trips_data_all.external_fhv_tripdata, error message: Parquet column 'DOlocationID' has type INT64 which does not match the target cpp_type DOUBLE.

Solution:

Fix the data type issue in data pipeline

Before injecting data into GCS, use astype and Int64 (which is different from int64 and accept both missing value and integer exist in the column) to cast the columns.

Something like:

df["PUlocationID"] = df.PUlocationID.astype("Int64")

df["DOlocationID"] = df.DOlocationID.astype("Int64")

NOTE: It is best to define the data type of all the columns in the Transformation section of the ETL pipeline before loading to BigQuery

