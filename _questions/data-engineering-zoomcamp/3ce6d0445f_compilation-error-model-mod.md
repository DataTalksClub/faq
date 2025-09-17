---
course: data-engineering-zoomcamp
id: 3ce6d0445f
question: 'Compilation Error : Model ''model.XXX'' (models/<model_path>/XXX.sql) depends
  on a source named ''<a table name>'' which was not found'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2830
---

Remember that you should modify accordingly your .sql models, to read from existing table names in BigQuery/postgres db

Example: select * from {{ source('staging',<your table name in the database>') }}

