---
id: 0812df9bf6
question: Docker - PostgreSQL Database directory appears to contain a database. Database system is shut down
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 820
---

When you see this in logs, your container with postgres is not accepting any requests, so if you attempt to connect, you'll get this error:

connection failed: server closed the connection unexpectedly

This probably means the server terminated abnormally before or while processing the request.

In this case, you need to delete the directory with data (the one you map to the container with the -v flag) and restart the container.

Solution 2:

If your data is critical, you may be able to reset the write-ahead lock from within the docker container (see )

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \

-p 5432:5432 \

--network pg-network \

postgres:13 \

/bin/bash -c 'gosu postgres pg_resetwal /var/lib/postgresql/data'

