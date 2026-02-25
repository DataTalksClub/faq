---
id: 61b2ad91aa
question: Run Local Cluster Spark in Windows 10 with CMD
sort_order: 46
---

1. Go to `%SPARK_HOME%\bin`

2. Run the following command to start the master:

   ```bash
   spark-class org.apache.spark.deploy.master.Master
   ```
   
   This will give you a URL of the form `spark://ip:port`.

3. Run the following command to start the worker, replacing `spark://ip:port` with the URL obtained from the previous step:

   ```bash
   spark-class org.apache.spark.deploy.worker.Worker spark://ip:port
   ```

4. Create a new Jupyter notebook and set up the Spark session:

   ```python
   spark = SparkSession.builder \
       .master("spark://{ip}:7077") \
       .appName('test') \
       .getOrCreate()
   ```

5. Check on the Spark UI to see the master, worker, and application running.