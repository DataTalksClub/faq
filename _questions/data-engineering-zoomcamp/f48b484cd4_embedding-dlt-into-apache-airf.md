---
course: data-engineering-zoomcamp
id: f48b484cd4
question: Embedding dlt into Apache Airflow
section: Workshop 1 - dlthub
sort_order: 4450
---

from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

import dlt

from my_dlt_pipeline import load_data  # Import your dlt pipeline function

default_args = {

"owner": "airflow",

"depends_on_past": False,

"start_date": datetime(2024, 2, 16),

"retries": 1,

"retry_delay": timedelta(minutes=5),

}

def run_dlt_pipeline():

pipeline = dlt.pipeline(

pipeline_name="my_pipeline",

destination="duckdb",  # Change this based on your database

dataset_name="my_dataset"

)

info = pipeline.run(load_data())

print(info)  # Logs for debugging

with DAG(

"dlt_airflow_pipeline",

default_args=default_args,

schedule_interval="@daily",

catchup=False,

) as dag:

run_dlt_task = PythonOperator(

task_id="run_dlt_pipeline",

python_callable=run_dlt_pipeline,

)

run_dlt_task

