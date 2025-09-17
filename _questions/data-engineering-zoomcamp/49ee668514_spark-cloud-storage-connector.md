---
id: 49ee668514
question: Spark Cloud Storage connector
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3520
---

: has anyone figured out how to read from GCP data lake instead of downloading all the taxi data again?

There’s a few extra steps to go into reading from GCS with PySpark

1.)  IMPORTANT: Download the Cloud Storage connector for Hadoop here:

As the name implies, this .jar file is what essentially connects PySpark with your GCS

2.) Move the .jar file to your Spark file directory. I installed Spark using homebrew on my MacOS machine and I had to create a /jars directory under "/opt/homebrew/Cellar/apache-spark/3.2.1/ (where my spark dir is located)

3.) In your Python script, there are a few extra classes you’ll have to import:

import pyspark

from pyspark.sql import SparkSession

from pyspark.conf import SparkConf

from pyspark.context import SparkContext

4.) You must set up your configurations before building your SparkSession. Here’s my code snippet:

conf = SparkConf() \

.setMaster('local[*]') \

.setAppName('test') \

.set("spark.jars", "/opt/homebrew/Cellar/apache-spark/3.2.1/jars/gcs-connector-hadoop3-latest.jar") \

.set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \

.set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "path/to/google_credentials.json")

sc = SparkContext(conf=conf)

sc._jsc.hadoopConfiguration().set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")

sc._jsc.hadoopConfiguration().set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")

sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.json.keyfile", "path/to/google_credentials.json")

sc._jsc.hadoopConfiguration().set("fs.gs.auth.service.account.enable", "true")

5.) Once you run that, build your SparkSession with the new parameters we’d just instantiated in the previous step:

spark = SparkSession.builder \

.config(conf=sc.getConf()) \

.getOrCreate()

6.) Finally, you’re able to read your files straight from GCS!

start-slave.sh: command not found

