---
course: data-engineering-zoomcamp
id: 0a431f8863
question: Spark BigQuery connector Automatic configuration
section: 'Module 5: pyspark'
sort_order: 3540
---

While creating a SparkSession using the config spark.jars.packages as com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.23.2

spark = SparkSession.builder.master('local').appName('bq').config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.23.2").getOrCreate()

automatically downloads the required dependency jars and configures the connector, removing the need to manage this dependency. More details available [here](https://github.com/GoogleCloudDataproc/spark-bigquery-connector)

