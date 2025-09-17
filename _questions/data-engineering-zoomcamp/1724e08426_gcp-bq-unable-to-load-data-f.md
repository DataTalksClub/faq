---
id: 1724e08426
question: GCP BQ - Unable to load data from external tables into a materialized table in BigQuery due to an invalid timestamp error that are added while appending data to the file in Google Cloud Storage
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2100
---

could not parse 'pickup_datetime' as timestamp for field pickup_datetime (position 2)

This error is caused by invalid data in the timestamp column. A way to identify the problem is to define the schema from the external table using string datatype. This enables the queries to work at which point we can filter out the invalid rows from the import to the materialised table and insert the fields with the timestamp data type.

