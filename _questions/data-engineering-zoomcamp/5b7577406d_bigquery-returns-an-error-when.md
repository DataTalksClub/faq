---
id: 5b7577406d
question: BigQuery returns an error when i try to run ‘dbt run’:
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3020
---

My taxi data was loaded into gcs with etl_web_to_gcs.py script that converts csv data into parquet. Then I placed raw data trips into external tables and when I executed dbt run I got an error message: Parquet column 'passenger_count' has type INT64 which does not match the target cpp_type DOUBLE. It is because several columns in files have different formats of data.

When I added df[col] = df[col].astype('Int64') transformation to the columns: passenger_count, payment_type, RatecodeID, VendorID, trip_type it went ok. Several people also faced this error and more about it you can read on the slack channel.

