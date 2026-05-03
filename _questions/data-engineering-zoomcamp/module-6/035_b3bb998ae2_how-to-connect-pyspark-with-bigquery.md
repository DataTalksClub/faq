---
id: b3bb998ae2
question: How do I connect PySpark to BigQuery?
sort_order: 35
---

Add the BigQuery connector to your SparkSession via `spark.jars.packages`. PySpark will download the matching jar from Maven Central on first run.

```python
from pyspark.sql import SparkSession

spark = (SparkSession.builder
    .master("local[*]")
    .appName("bq")
    .config("spark.jars.packages",
            "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.42.0")
    .getOrCreate())
```

Pick a connector version that matches your Spark / Scala version (the `_2.12` suffix is the Scala build target). Check the latest at the [Spark BigQuery connector releases](https://github.com/GoogleCloudDataproc/spark-bigquery-connector).

For credentials, set `GOOGLE_APPLICATION_CREDENTIALS` in your environment to the path of your service account JSON before launching Spark — the connector picks it up automatically.

For the read/write API once the connector is loaded, see the dedicated Spark + BigQuery FAQ.
