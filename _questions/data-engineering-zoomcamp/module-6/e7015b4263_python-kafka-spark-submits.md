---
id: e7015b4263
question: 'Python Kafka: ./spark-submit.sh streaming.py - How to check why Spark master
  connection fails'
sort_order: 4080
---

Start a new terminal

Run: docker ps

Copy the CONTAINER ID of the spark-master container

Run: docker exec -it <spark_master_container_id> bash

Run: cat logs/spark-master.out

Check for the log when the error happened

Google the error message from there

