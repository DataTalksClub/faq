---
course: data-engineering-zoomcamp
id: 155949a31a
question: GCP BQ ML - Unable to run command (shown in video) to export ML model from
  BQ to GCS
section: 'Module 3: Data Warehousing'
sort_order: 2260
---

Issue: Tried running command to export ML model from BQ to GCS from Week 3

bq --project_id taxi-rides-ny extract -m nytaxi.tip_model gs://taxi_ml_model/tip_model

It is failing on following error:

BigQuery error in extract operation: Error processing job Not found: Dataset was not found in location US

I verified the BQ data set and gcs bucket are in the same region- us-west1. Not sure how it gets location US. I couldn’t find the solution yet.

Solution:  Please enter correct project_id and gcs_bucket folder address. My gcs_bucket folder address is

gs://dtc_data_lake_optimum-airfoil-376815/tip_model

