---
id: ef201a0b0b
question: Docker - Could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 680
---

$ docker run -it\

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="admin" \

-e POSTGRES_DB="ny_taxi" \

-v "/mnt/path/to/ny_taxi_postgres_data":"/var/lib/postgresql/data" \

-p 5432:5432 \

postgres:13

CCW

The files belonging to this database system will be owned by user "postgres".

This use The database cluster will be initialized with locale "en_US.utf8".

The default database encoding has accordingly been set to "UTF8".

xt search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... initdb: f

error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted  volume

One way to solve this issue is to create a local docker volume and map it to postgres data directory /var/lib/postgresql/data

The input dtc_postgres_volume_local must match in both commands below

$ docker volume create --name dtc_postgres_volume_local -d local

$ docker run -it\

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v dtc_postgres_volume_local:/var/lib/postgresql/data \

-p 5432:5432\

postgres:13

To verify the above command works in (WSL2 Ubuntu 22.04, verified 2024-Jan), go to the Docker Desktop app and look under Volumes - dtc_postgres_volume_local would be listed there. The folder ny_taxi_postgres_data would however be empty, since we used an alternative config.

An alternate error could be:

initdb: error: directory "/var/lib/postgresql/data" exists but is not empty

If you want to create a new database system, either remove or empty the directory "/var/lib/postgresql/data" or run initdb

