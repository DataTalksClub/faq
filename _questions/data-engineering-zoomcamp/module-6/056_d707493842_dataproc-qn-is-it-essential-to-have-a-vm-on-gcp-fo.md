---
id: d707493842
question: 'Dataproc Qn: Is it essential to have a VM on GCP for running Dataproc and
  submitting jobs?'
sort_order: 56
---

No, you can submit a job to Dataproc from your local computer by installing and configuring `gsutil`. For installation instructions, visit [https://cloud.google.com/storage/docs/gsutil_install](https://cloud.google.com/storage/docs/gsutil_install).

You can execute the following command from your local computer:

```bash
gcloud dataproc jobs submit pyspark \
  --cluster=de-zoomcamp-cluster \
  --region=europe-west6 \
  gs://dtc_data_lake_de-zoomcamp-nytaxi/code/06_spark_sql.py \
  -- \
  --input_green=gs://dtc_data_lake_de-zoomcamp-nytaxi/pq/green/2020/*/ \
  --input_yellow=gs://dtc_data_lake_de-zoomcamp-nytaxi/pq/yellow/2020/*/ \
  --output=gs://dtc_data_lake_de-zoomcamp-nytaxi/report-2020
```