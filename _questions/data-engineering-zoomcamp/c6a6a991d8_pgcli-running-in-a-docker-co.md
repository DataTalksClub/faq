---
id: c6a6a991d8
question: PGCLI - running in a Docker container
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1140
---

In case running pgcli  locally causes issues or you do not want to install it locally you can use it running in a Docker container instead.

Below the usage with values used in the videos of the course for:

network name (docker network)

postgres related variables for pgcli

Hostname

Username

Port

Database name

$ docker run -it --rm --network pg-network ai2ys/dockerized-pgcli:4.0.1

175dd47cda07:/# pgcli -h pg-database -U root -p 5432 -d ny_taxi

Password for root:

Server: PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)

Version: 4.0.1

Home:

root@pg-database:ny_taxi> \dt

+--------+------------------+-------+-------+

| Schema | Name             | Type  | Owner |

|--------+------------------+-------+-------|

| public | yellow_taxi_data | table | root  |

+--------+------------------+-------+-------+

SELECT 1

Time: 0.009s

root@pg-database:ny_taxi>

