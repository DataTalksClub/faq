---
id: 8bfd724e4f
question: Compilation Error in test accepted_values_stg_green_tripdata_Payment_type__False___var_payment_type_values_ (models/staging/schema.yml)  'NoneType' object is not iterable
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2780
---

> in macro test_accepted_values (tests/generic/builtin.sql)

> called by test accepted_values_stg_green_tripdata_Payment_type__False___var_payment_type_values_ (models/staging/schema.yml)

Remember that you have to add to dbt_project.yml the vars:

vars:

payment_type_values: [1, 2, 3, 4, 5, 6]

