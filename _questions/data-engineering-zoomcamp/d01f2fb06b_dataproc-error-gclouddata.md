---
id: d01f2fb06b
question: Dataproc - ERROR: (gcloud.dataproc.jobs.submit.pyspark) The required property [project] is not currently set. It can be set on a per-command basis by re-running your command with the [--project] flag.
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3720
---

Fix is to set the flag like the error states. Get your project ID from your dashboard and set it like so:

gcloud dataproc jobs submit pyspark \

--cluster=my_cluster \

--region=us-central1 \

--project=my-dtc-project-1010101 \

gs://my-dtc-bucket-id/code/06_spark_sql.py

-- \

…

