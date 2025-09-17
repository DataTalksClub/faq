---
id: b209edb213
question: DBT - Error: “404 Not found: Dataset <dataset_name>:<dbt_schema_name> was not found in location EU” after building from stg_green_tripdata.sql
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3100
---

In the step in  (DE Zoomcamp 4.3.1 - Build the First dbt Models), after creating `stg_green_tripdata.sql` and clicking `build`, I encountered an error saying dataset not found in location EU. The default location for dbt Bigquery is the US, so when generating the new Bigquery schema for dbt, unless specified, the schema locates in the US.

Solution:

Turns out I forgot to specify Location to be `EU` when adding connection details.

Develop -> Configure Cloud CLI -> Projects -> taxi_rides_ny -> (connection) Bigquery -> Edit -> Location (Optional) -> type `EU` -> Save

