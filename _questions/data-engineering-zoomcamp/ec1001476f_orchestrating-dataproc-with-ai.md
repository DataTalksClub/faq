---
course: data-engineering-zoomcamp
id: ec1001476f
question: Orchestrating DataProc with Airflow
section: Project
sort_order: 4260
---

Give the following roles to you service account:

DataProc Administrator

Service Account User (explanation )

Use DataprocSubmitPySparkJobOperator, DataprocDeleteClusterOperator and  DataprocCreateClusterOperator.

When using  DataprocSubmitPySparkJobOperator, do not forget to add:

dataproc_jars = ["gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.24.0.jar"]

Because DataProc does not already have the BigQuery Connector.

