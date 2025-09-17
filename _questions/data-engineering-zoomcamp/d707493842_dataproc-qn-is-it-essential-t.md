---
id: d707493842
question: Dataproc Qn: Is it essential to have a VM on GCP for running Dataproc and submitting jobs ?
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3830
---

Ans: No, you can submit a job to DataProc from your local computer by installing gsutil () and configuring it. Then, you can execute the following command from your local computer.

gcloud dataproc jobs submit pyspark \

--cluster=de-zoomcamp-cluster \

--region=europe-west6 \

gs://dtc_data_lake_de-zoomcamp-nytaxi/code/06_spark_sql.py \

-- \

--input_green=gs://dtc_data_lake_de-zoomcamp-nytaxi/pq/green/2020/*/ \

--input_yellow=gs://dtc_data_lake_de-zoomcamp-nytaxi/pq/yellow/2020/*/ \

--output=gs://dtc_data_lake_de-zoomcamp-nytaxi/report-2020 (edited)

