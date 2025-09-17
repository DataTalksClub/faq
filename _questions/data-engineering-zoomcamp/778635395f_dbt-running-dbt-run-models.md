---
id: 778635395f
question: DBT - Running dbt run --models stg_green_tripdata --var 'is_test_run: false' is not returning anything:
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3030
---

Use the syntax below instead if the code in the tutorial is not working.

dbt run --select stg_green_tripdata --vars '{"is_test_run": false}'

