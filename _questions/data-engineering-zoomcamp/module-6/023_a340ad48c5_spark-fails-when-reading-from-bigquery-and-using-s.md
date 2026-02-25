---
id: a340ad48c5
question: Spark fails when reading from BigQuery and using `.show()` on `SELECT` queries
sort_order: 23
---



I got it working using `gcs-connector-hadoop-2.2.5-shaded.jar` and Spark 3.1.

I also added the `google_credentials.json` and `.p12` to authenticate with GCS. These files are downloadable from the GCP Service account.

To create the SparkSession:

```python
spark = SparkSession.builder.master('local[*]') \
    .appName('spark-read-from-bigquery') \
    .config('BigQueryProjectId', 'razor-project-xxxxxxx') \
    .config('BigQueryDatasetLocation', 'de_final_data') \
    .config('parentProject', 'razor-project-xxxxxxx') \
    .config("google.cloud.auth.service.account.enable", "true") \
    .config("credentialsFile", "google_credentials.json") \
    .config("GcpJsonKeyFile", "google_credentials.json") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "2g") \
    .config("spark.memory.offHeap.enabled", True) \
    .config("spark.memory.offHeap.size", "5g") \
    .config('google.cloud.auth.service.account.json.keyfile', "google_credentials.json") \
    .config("fs.gs.project.id", "razor-project-xxxxxxx") \
    .config("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS") \
    .getOrCreate()
```