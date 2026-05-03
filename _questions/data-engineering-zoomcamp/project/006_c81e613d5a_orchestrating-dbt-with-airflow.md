---
id: c81e613d5a
question: Orchestrating dbt with Airflow
sort_order: 6
---

The trial dbt account provides access to the dbt API. A job will still need to be added manually. Airflow can run the job using a Python operator that calls the API. You will need to provide an API key, job ID, etc., and be careful not to commit this information to GitHub.

- Detailed explanation: [dbt and Airflow Spiritual Alignment](https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment)
- Source code example: [GitHub dbt Cloud Example](https://github.com/sungchun12/airflow-toolkit/blob/95d40ac76122de337e1b1cdc8eed35ba1c3051ed/dags/examples/dbt_cloud_example.py)