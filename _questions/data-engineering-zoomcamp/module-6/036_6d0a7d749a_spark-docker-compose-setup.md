---
id: 6d0a7d749a
question: Spark docker-compose setup
sort_order: 36
---

To run Spark in a Docker setup:

1. **Build Bitnami Spark Docker**
   
   a. Clone the Bitnami repository using the command:
   
   ```bash
   git clone https://github.com/bitnami/containers.git
   ```
   
   *(Tested on commit 9cef8b892d29c04f8a271a644341c8222790c992)*
   
   b. Edit the file `bitnami/spark/3.3/debian-11/Dockerfile` and update the Java and Spark version as follows:
   
   ```
   "python-3.10.10-2-linux-${OS_ARCH}-debian-11" 
   "java-17.0.5-8-3-linux-${OS_ARCH}-debian-11" 
   ```
   
   Reference: [GitHub](https://github.com/bitnami/containers/issues/13409)

   c. Build the Docker image by navigating to the above directory and running the Docker build command:
   
   ```bash
   cd bitnami/spark/3.3/debian-11/
   docker build -t spark:3.3-java-17 .
   ```

2. **Run Docker Compose**

   Use the following `docker-compose.yml` file:

   ```yaml
   version: '2'

   services:

     spark:
       image: spark:3.3-java-17
       environment:
         - SPARK_MODE=master
         - SPARK_RPC_AUTHENTICATION_ENABLED=no
         - SPARK_RPC_ENCRYPTION_ENABLED=no
         - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
         - SPARK_SSL_ENABLED=no
       volumes:
         - "./:/home/jovyan/work:rw"
       ports:
         - '8080:8080'
         - '7077:7077'

     spark-worker:
       image: spark:3.3-java-17
       environment:
         - SPARK_MODE=worker
         - SPARK_MASTER_URL=spark://spark:7077
         - SPARK_WORKER_MEMORY=1G
         - SPARK_WORKER_CORES=1
         - SPARK_RPC_AUTHENTICATION_ENABLED=no
         - SPARK_RPC_ENCRYPTION_ENABLED=no
         - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
         - SPARK_SSL_ENABLED=no
       volumes:
         - "./:/home/jovyan/work:rw"
       ports:
         - '8081:8081'

     spark-nb:
       image: jupyter/pyspark-notebook:java-17.0.5
       environment:
         - SPARK_MASTER_URL=spark://spark:7077
       volumes:
         - "./:/home/jovyan/work:rw"
       ports:
         - '8888:8888'
         - '4040:4040'
   ```

   Run the command to deploy Docker Compose:

   ```bash
   docker-compose up
   ```

   Access the Jupyter notebook using the link logged in Docker Compose logs.

   The Spark master URL is `spark://spark:7077`. 