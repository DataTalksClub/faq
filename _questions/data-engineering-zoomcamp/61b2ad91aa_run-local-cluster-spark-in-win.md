---
id: 61b2ad91aa
question: Run Local Cluster Spark in Windows 10 with CMD
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3730
---

Go to %SPARK_HOME%\bin

Run spark-class org.apache.spark.deploy.master.Master to run the master. This will give you a URL of the form spark://ip:port

Run spark-class org.apache.spark.deploy.worker.Worker spark://ip:port to run the worker. Make sure you use the URL you obtained in step 2.

Create a new Jupyter notebook:

spark = SparkSession.builder \

.master("spark://{ip}:7077") \

.appName('test') \

.getOrCreate()

Check on Spark UI the master, worker and app.

