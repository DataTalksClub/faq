---
id: 3cc457b0de
question: DBT - I ran dbt run without specifying variable which gave me a table of 100 rows. I ran again with the variable value specified but my table still has 100 rows in BQ.
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2690
---

Remove the dataset from BigQuery created by dbt and run again (with test disabled) to ensure the dataset created has all the rows.

DBT - Why am I getting a new dataset after running my CI/CD Job? / What is this new dbt dataset in BigQuery?

Answer: when you create the CI/CD job, under ‘Compare Changes against an environment (Deferral) make sure that you select ‘ No; do not defer to another environment’ - otherwise dbt won’t merge your dev models into production models; it will create a new environment called ‘dbt_cloud_pr_number of pull request’

![Image](images/data-engineering-zoomcamp/image_71e1a1ed.png)

