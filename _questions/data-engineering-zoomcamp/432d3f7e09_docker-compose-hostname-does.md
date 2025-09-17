---
id: 432d3f7e09
question: Docker-Compose - Hostname does not resolve
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 870
---

It returns --> Error response from daemon: network 66ae65944d643fdebbc89bd0329f1409dec2c9e12248052f5f4c4be7d1bdc6a3 not found

Try:

docker ps -a to see all the stopped & running containers

d to nuke all the containers

Try: docker-compose up -d again ports

On localhost:8080 server → Unable to connect to server: could not translate host name 'pg-database' to address: Name does not resolve

Try: new host name, best without “ - ” e.g. pgdatabase

And on docker-compose.yml, should specify docker network & specify the same network in both  containers

services:

pgdatabase:

image: postgres:13

environment:

- POSTGRES_USER=root

- POSTGRES_PASSWORD=root

- POSTGRES_DB=ny_taxi

volumes:

- "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"

ports:

- "5431:5432"

networks:

- pg-network

pgadmin:

image: dpage/pgadmin4

environment:

- PGADMIN_DEFAULT_EMAIL=admin@admin.com

- PGADMIN_DEFAULT_PASSWORD=root

ports:

- "8080:80"

networks:

- pg-network

networks:

pg-network:

name: pg-network

