---
id: 01092d660a
question: Spark Standalone Mode on Windows
sort_order: 31
---

To set up Spark in standalone mode on Windows, follow these steps:

1. Open a CMD terminal in administrator mode.

2. Navigate to your Spark home directory:
   
   ```bash
   cd %SPARK_HOME%
   ```

3. Start a master node:
   
   ```bash
   bin\spark-class org.apache.spark.deploy.master.Master
   ```

4. Start a worker node:
   
   ```bash
   bin\spark-class org.apache.spark.deploy.worker.Worker spark://<master_ip>:<port> --host <IP_ADDR>
   ```
   
   Example:
   
   ```bash
   bin\spark-class org.apache.spark.deploy.worker.Worker spark://localhost:7077 --host <IP_ADDR>
   ```

   - `spark://<master_ip>:<port>`: Copy the address from the previous command. For example, `spark://localhost:7077`
   - Use `--host <IP_ADDR>` if you want to run the worker on a different machine. You can leave it empty for local setup.

5. Access the Spark UI through `localhost:8080`.