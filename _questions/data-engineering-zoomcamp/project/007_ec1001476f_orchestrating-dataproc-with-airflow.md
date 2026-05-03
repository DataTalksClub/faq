---
id: ec1001476f
question: Orchestrating DataProc with Airflow
sort_order: 7
---

For orchestrating DataProc with Airflow, you can refer to the following documentation:

- [Airflow DataProc Operators - API Docs](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html)
- [Airflow DataProc Operators - Module Docs](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_modules/airflow/providers/google/cloud/operators/dataproc.html)

### Roles for Service Account

Ensure that you assign the following roles to your service account:

- **DataProc Administrator**
- **Service Account User**
  
  For more details, see the explanation on [Stack Overflow](https://stackoverflow.com/questions/63941429/user-not-authorized-to-act-as-service-account-when-using-workload-identity).

### Operators to Use

- `DataprocSubmitPySparkJobOperator`
- `DataprocDeleteClusterOperator`
- `DataprocCreateClusterOperator`

### Important Note

When using `DataprocSubmitPySparkJobOperator`, make sure to add the BigQuery Connector, as DataProc does not include it by default:

```python
  dataproc_jars = ["gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.24.0.jar"]
```