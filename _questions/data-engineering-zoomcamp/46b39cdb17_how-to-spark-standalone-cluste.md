---
course: data-engineering-zoomcamp
id: 46b39cdb17
question: How to spark standalone cluster is run on windows OS
section: 'Module 5: pyspark'
sort_order: 3670
---

Change the working directory to the spark directory:

if you have setup up your SPARK_HOME variable, use the following;

cd %SPARK_HOME%

if not, use the following;

cd <path to spark installation>

Creating a Local Spark Cluster

To start Spark Master:

bin\spark-class org.apache.spark.deploy.master.Master --host localhost

Starting up a cluster:

bin\spark-class org.apache.spark.deploy.worker.Worker spark://localhost:7077 --host localhost

