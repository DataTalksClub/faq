---
course: data-engineering-zoomcamp
id: edcc24a810
question: 'Docker-Compose -  Data retention (could not translate host name "pg-database"
  to address: Name or service not known)'
section: 'Module 1: Docker and Terraform'
sort_order: 860
---

![Image](images/data-engineering-zoomcamp/image_dc508dc3.png)

Make sure postgres database is running.

​​Use the command to start containers in detached mode: docker-compose up -d

(data-engineering-zoomcamp) hw % docker compose up -d

[+] Running 2/2

⠿ Container pg-admin     Started                                                                                                                                                                      0.6s

⠿ Container pg-database  Started

To view the containers use: docker ps.

(data-engineering-zoomcamp) hw % docker ps

CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                           NAMES

faf05090972e   postgres:13      "docker-entrypoint.s…"   39 seconds ago   Up 37 seconds   0.0.0.0:5432->5432/tcp          pg-database

6344dcecd58f   dpage/pgadmin4   "/entrypoint.sh"         39 seconds ago   Up 37 seconds   443/tcp, 0.0.0.0:8080->80/tcp   pg-admin
hw

To view logs for a container: docker logs <containerid>

(data-engineering-zoomcamp) hw % docker logs faf05090972e

PostgreSQL Database directory appears to contain a database; Skipping initialization

2022-01-25 05:58:45.948 UTC [1] LOG:  starting PostgreSQL 13.5 (Debian 13.5-1.pgdg110+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit

2022-01-25 05:58:45.948 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432

2022-01-25 05:58:45.948 UTC [1] LOG:  listening on IPv6 address "::", port 5432

2022-01-25 05:58:45.954 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"

2022-01-25 05:58:45.984 UTC [28] LOG:  database system was interrupted; last known up at 2022-01-24 17:48:35 UTC

2022-01-25 05:58:48.581 UTC [28] LOG:  database system was not properly shut down; automatic recovery in

progress

2022-01-25 05:58:48.602 UTC [28] LOG:  redo starts at 0/872A5910

2022-01-25 05:59:33.726 UTC [28] LOG:  invalid record length at 0/98A3C160: wanted 24, got 0

2022-01-25 05:59:33.726 UTC [28

] LOG:  redo done at 0/98A3C128

2022-01-25 05:59:48.051 UTC [1] LOG:  database system is ready to accept connections

If docker ps doesn’t show pgdatabase running, run: docker ps -a

This should show all containers, either running or stopped.

Get the container id for pgdatabase-1, and run

After executing `docker-compose up` - if you lose database data and are unable to successfully execute your Ingestion script (to re-populate your database) but receive the following error:

sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not translate host name /data_pgadmin:/var/lib/pgadmin"pg-database" to address: Name or service not known

Docker compose is creating its own default network since it is no longer specified in a docker execution command or file. Docker Compose will emit to logs the new network name. See the logs after executing `docker compose up` to find the network name and change the network name argument in your Ingestion script.

If problems persist with pgcli, we can use HeidiSQL

Krishna Anand

