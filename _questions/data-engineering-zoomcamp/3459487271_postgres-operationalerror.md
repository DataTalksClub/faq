---
id: 3459487271
question: Postgres - OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  role "root" does not exist
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1210
---

Can happen when connecting via pgcli

pgcli -h localhost -p 5432 -U root -d ny_taxi

Or while uploading data via the connection in jupyter notebook

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

This can happen when Postgres is already installed on your computer. Changing the port can resolve that (e.g. from 5432 to 5431).

Also, you could change port from 5432:5432 to 5431:5432

Other solution that worked:

Changing `POSTGRES_USER=juroot` to `PGUSER=postgres`

Based on this:

Also `docker compose down`, removing folder that had postgres volume, running `docker compose up` again.

