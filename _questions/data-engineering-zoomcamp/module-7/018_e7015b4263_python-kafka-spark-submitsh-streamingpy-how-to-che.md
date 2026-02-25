---
id: e7015b4263
question: 'Python Kafka: ./spark-submit.sh streaming.py - How to check why Spark master
  connection fails'
sort_order: 18
---

- Start a new terminal.

- Run the following command to list running containers:

  ```bash
  docker ps
  ```

- Copy the `CONTAINER ID` of the `spark-master` container.

- Execute the following command to access the container's shell:

  ```bash
  docker exec -it <spark_master_container_id> bash
  ```

- Run this command to view the Spark master logs:

  ```bash
  cat logs/spark-master.out
  ```

- Check the log for the timestamp when the error occurred.

- Search the error message online for further troubleshooting.