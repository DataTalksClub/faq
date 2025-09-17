---
course: data-engineering-zoomcamp
id: e596dc3cbe
question: DBT - When executing dbt run after installing dbt-utils latest version i.e.,
  1.0.0 warning has generated
section: 'Module 4: analytics engineering with dbt'
sort_order: 2600
---

Error: `dbt_utils.surrogate_key` has been replaced by `dbt_utils.generate_surrogate_key`

Fix:

Replace dbt_utils.surrogate_key  with dbt_utils.generate_surrogate_key in stg_green_tripdata.sql

