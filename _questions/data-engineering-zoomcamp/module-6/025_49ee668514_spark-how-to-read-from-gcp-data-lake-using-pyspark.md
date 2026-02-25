---
id: 49ee668514
question: 'Spark: How to read from GCP data lake using PySpark?'
sort_order: 25
---

There are a few steps to read from Google Cloud Storage (GCS) using PySpark:

1. **Download the Cloud Storage connector for Hadoop**
   - You can download it [here](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage#clusters).
   - This `.jar` file connects PySpark with GCS.

2. **Move the .jar file to your Spark file directory**
   - If you installed Spark using Homebrew on MacOS, create a `/jars` directory under your Spark directory, e.g., `/opt/homebrew/Cellar/apache-spark/3.2.1/jars`.

3. **Import necessary classes in your Python script**
   ```python
   import pyspark
   from pyspark.sql import SparkSession
   from pyspark.conf import SparkConf
   from pyspark.context import SparkContext
   ```

4. **Set up your configurations before building the SparkSession**
   ```python
   conf = SparkConf() \
       .setMaster('local[*]') \
       .setAppName('test') \
       .set("spark.jars", "/opt/homebrew/Cellar/apache-spark/3.2.1/jars/gcs-connector-hadoop3-latest.jar") \
       .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
       .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "path/to/google_credentials.json")
   
   sc = SparkContext(conf=conf)

   sc._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
   sc._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
   sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.json.keyfile", "path/to/google_credentials.json")
   sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.enable", "true")
   ```

5. **Build your SparkSession with the new configurations**
   ```python
   spark = SparkSession.builder \
       .config(conf=sc.getConf()) \
       .getOrCreate()
   ```

6. **You can now read files directly from GCS!**

Note: If you encounter `start-slave.sh: command not found`, ensure Spark is correctly installed and paths are set.