---
course: data-engineering-zoomcamp
id: 0fbc18e0f2
question: 'DBT - Error on building fact_trips.sql: Parquet column ''ehail_fee'' has
  type DOUBLE which does not match the target cpp_type INT64. File: gs://<gcs bucket>/<table>/green_taxi_2019-01.parquet")'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2960
---

The two solution above don’t work for me - I used the line below in `stg_green_trips.sql` to replace the original ehail_fee line:

`{{ dbt.safe_cast('ehail_fee',  api.Column.translate_type("numeric"))}} as ehail_fee,`

