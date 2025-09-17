---
course: data-engineering-zoomcamp
id: 01092d660a
question: Spark Standalone Mode on Windows
section: 'Module 5: pyspark'
sort_order: 3580
---

Open a CMD terminal in administrator mode

cd %SPARK_HOME%

Start a master node: bin\spark-class org.apache.spark.deploy.master.Master

Start a worker node: bin\spark-class org.apache.spark.deploy.worker.Worker spark://<master_ip>:<port> --host <IP_ADDR>

bin/spark-class org.apache.spark.deploy.worker.Worker spark://localhost:7077 --host <IP_ADDR>

spark://<master_ip>:<port>: copy the address from the previous command, in my case it was spark://localhost:7077

Use --host <IP_ADDR> if you want to run the worker on a different machine. For now leave it empty.

Now you can access Spark UI through localhost:8080

