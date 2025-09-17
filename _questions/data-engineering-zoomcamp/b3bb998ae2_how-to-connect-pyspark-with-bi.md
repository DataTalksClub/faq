---
course: data-engineering-zoomcamp
id: b3bb998ae2
question: How to connect Pyspark with BigQuery?
section: Project
sort_order: 4290
---

The following line should be included in pyspark configuration

# Example initialization of SparkSession variable

spark = (SparkSession.builder

.master(...)

.appName(...)

# Add the following configuration

.config("spark.jars.packages", "com.google.cloud.spark:spark-3.5-bigquery:0.37.0")

)

