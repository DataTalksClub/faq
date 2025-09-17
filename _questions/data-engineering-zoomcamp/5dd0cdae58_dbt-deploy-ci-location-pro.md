---
id: 5dd0cdae58
question: DBT Deploy + CI - Location Problems on BigQuery
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3080
---

When you are creating the pull request and running the CI, dbt is creating a new schema on BIgQuery. By default that new schema will be created on ‘US’ location, if you have your dataset, schemas and tables on ‘EU’ that will generate an error and the pull request will not be accepted. To change that location to ‘EU’ on the connection to BigQuery from dbt we need to add the location ‘EU’ on the connection optional settings:

Dbt -> project -> settings -> connection BIgQuery -> OPtional Settings -> Location -> EU

