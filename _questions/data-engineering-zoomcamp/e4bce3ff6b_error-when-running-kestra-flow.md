---
course: data-engineering-zoomcamp
id: e4bce3ff6b
question: Error when running Kestra flow connecting to postgres.
section: 'Module 2: Workflow Orchestration'
sort_order: 1840
---

Error: org.postgresql.util.psqlexception the connection attempt failed due to this config on kestra flow -> jdbc:postgresql://host.docker.internal:5432/postgres-zoomcamp

Solution: Just replace host.docker.internal for the name of the service for postgres in docker compose.

—---

I also encountered a similar error as above, slightly different error message:

org.postgresql.util.PSQLException: The connection attempt failed. 2025-01-29 22:52:22.281 green_create_table The connection attempt failed. host.docker.internal

I could download my dataset by executing my flow, but when i wanted to ingest it to the pg database, the connection to pg failed.

The main issue was that the pg database url is different for linux than the url in the tutorial. Namely, instead of host.docker.internal, linux users will use the service or container name for postgres, which for me was just postgres.

url: jdbc:postgresql://postgres:5432/kestra

Voila. Also, make sure to double check your pg database name. Mine was kestra in the docker compose file, whereas in the tutorial they had named it postgres-zoomcamp.

