---
id: 6d0a7d749a
question: Spark docker-compose setup
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3630
---

To run spark in docker setup

1. Build bitnami spark docker

a. clone bitnami repo using command

git clone https://github.com/bitnami/containers.git

(tested on commit 9cef8b892d29c04f8a271a644341c8222790c992)

b. edit file `bitnami/spark/3.3/debian-11/Dockerfile` and update java and spark version as following

"python-3.10.10-2-linux-${OS_ARCH}-debian-11" \

"java-17.0.5-8-3-linux-${OS_ARCH}-debian-11" \

reference: https://github.com/bitnami/containers/issues/13409

c. build docker image by navigating to above directory and running docker build command

navigate cd bitnami/spark/3.3/debian-11/

build command docker build -t spark:3.3-java-17 .

2. run docker compose

using following file

```yaml docker-compose.yml

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

run command to deploy docker compose

docker-compose up

Access jupyter notebook using link logged in docker compose logs

Spark master url is spark://spark:7077

