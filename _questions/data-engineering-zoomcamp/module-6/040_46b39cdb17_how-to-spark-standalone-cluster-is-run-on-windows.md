---
id: 46b39cdb17
question: How to spark standalone cluster is run on windows OS
sort_order: 40
---

- Change the working directory to the Spark directory:

  - If you have set up your `SPARK_HOME` variable, use the following:
    
    ```bash
    cd %SPARK_HOME%
    ```

  - If not, use the following:

    ```bash
    cd <path to spark installation>
    ```

- Creating a Local Spark Cluster:

  1. To start Spark Master:
  
     ```bash
     bin\spark-class org.apache.spark.deploy.master.Master --host localhost
     ```
  
  2. Starting up a cluster:
     
     ```bash
     bin\spark-class org.apache.spark.deploy.worker.Worker spark://localhost:7077 --host localhost
     ```