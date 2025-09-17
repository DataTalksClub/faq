---
course: data-engineering-zoomcamp
id: d3c860aa46
question: Docker-Compose - Postgres container fails to launch with exit code (1) when
  attempting to compose
section: 'Module 1: Docker and Terraform'
sort_order: 1000
---

This happens due to the Postgres database not being initialized before running docker-compose up -d. There are other potential ways around it ([thread](https://forums.docker.com/t/one-of-the-postgres-containers-stops-as-soon-as-it-starts/74714/3)) but you can simply initialize the database first and the compose will work afterward.

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v $(pwd)/ny_taxi_data:/var/lib/postgresql/data \

-p 5432:5432 \

--network=pg-network \

--name=pg_database \

postgres:13

