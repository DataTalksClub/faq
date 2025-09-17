---
course: data-engineering-zoomcamp
id: 1700cb2bd4
question: Docker - ingestion when using docker-compose could not translate host name
section: 'Module 1: Docker and Terraform'
sort_order: 780
---

Typical error:n.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "pgdatabase" to address: Name or service not known

When running docker-compose up -d see which network is created and use this for the ingestions script instead of pg-network and see the name of the database to use instead of pgdatabase

E.g.:

pg-network becomes 2docker_default

