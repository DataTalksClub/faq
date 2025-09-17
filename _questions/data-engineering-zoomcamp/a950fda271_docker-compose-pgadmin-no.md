---
course: data-engineering-zoomcamp
id: a950fda271
question: Docker-Compose + PgAdmin – no database in PgAdmin
section: 'Module 1: Docker and Terraform'
sort_order: 880
---

When you login into PgAdmin and see empty database, the solution below can help:

When you run

docker-compose up

and at the same time

docker build -t taxi_ingest:v001 .

with

docker run -it \

--network=pg-network \ ← <---- NETWORK NAME IS THE SAME AS THAT CREATED BY DOCKER COMPOSE

taxi_ingest:v001 \

--user=postgres \

--password=postgres \

--host=db \

--port=5432 \

--db=ny_taxi \

--table_name=green_tripdata \

--url=${URL}

It’s important to use the same --network which states in the file docker-compose.yaml (networks, as mentioned above).  OR The file docker-compose.yaml might not specify a network, as in the example below.

services:

db:

container_name: postgres

image: postgres:17-alpine

environment:

…

ports:

- '5433:5432'

volumes:

- …

pgadmin:

container_name: pgadmin

image: dpage/pgadmin4:latest

environment:

…

ports:

- "8080:80"

volumes:

- …

volumes:

vol-pgdata:

name: vol-pgdata

vol-pgadmin_data:

name: vol-pgadmin_data

In this case, the network name is generated automatically: The name of the directory containing the docker-compose.yaml file in lowercase + _default.

You can find the network’s name during running docker-compose up

pg-database Pulling
 pg-database Pulled
 Network week_1_default  Creating <-- THIS ONE
 Network week_1_default  Created

