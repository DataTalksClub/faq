---
id: 155949a31a
question: 'GCP BQ ML: Unable to run command (shown in video) to export ML model from
  BQ to GCS'
sort_order: 27
---

**Issue:**

Tried running command to export ML model from BQ to GCS from Week 3:

```bash
bq --project_id taxi-rides-ny extract -m nytaxi.tip_model gs://taxi_ml_model/tip_model
```

It is failing with the following error:

```
BigQuery error in extract operation: Error processing job Not found: Dataset was not found in location US
```

I verified the BQ dataset and GCS bucket are in the same region, `us-west1`. Not sure why it gets location `US`. I couldn’t find the solution yet.

**Solution:**

Please ensure the following:

- Enter the correct `project_id` and `gcs_bucket` folder address.
- Example of a correct GCS bucket folder address:
  
  ```text
  gs://dtc_data_lake_optimum-airfoil-376815/tip_model
  ```