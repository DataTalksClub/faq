---
id: 0a431f8863
question: 'Spark: BigQuery connector Automatic configuration'
sort_order: 24
---

To automatically configure the Spark BigQuery connector, you can create a `SparkSession` by specifying the `spark.jars.packages` configuration.

```python
spark = SparkSession.builder 
    .master('local') 
    .appName('bq') 
    .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.23.2") 
    .getOrCreate()
```

This approach automatically downloads the required dependency jars and configures the connector, eliminating the need to manually manage this dependency. More details are available [here](https://github.com/GoogleCloudDataproc/spark-bigquery-connector).