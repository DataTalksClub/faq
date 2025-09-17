---
course: data-engineering-zoomcamp
id: 12dffd5b1a
question: 'PGCLI -connection failed: FATAL: password authentication failed for user
  "root"'
section: 'Module 1: Docker and Terraform'
sort_order: 1120
---

The error above was faced continually despite inputting the correct password

Solution

Option 1: Stop the PostgreSQL service on Windows

Option 2 (using WSL): Completely uninstall Protgres 12 from Windows and install postgresql-client on WSL (sudo apt install postgresql-client-common postgresql-client libpq-dev)

Option 3: Change the port of the docker container

Option 4: NEW SOLUTION: 27/01/2024

PGCLI -connection failed: FATAL:  password authentication failed for user "root"

If you’ve got the error above, it’s probably because you were just like me, closed the connection to the Postgres:13 image in the previous step of the tutorial, which is

docker run -it \

-e POSTGRES_USER=root \

-e POSTGRES_PASSWORD=root \

-e POSTGRES_DB=ny_taxi \

-v d:/git/data-engineering-zoomcamp/week_1/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \

-p 5432:5432 \

postgres:13

So keep the database connected and you will be able to implement all the next steps of the tutorial.

![Image](images/data-engineering-zoomcamp/image_cb7165fc.png)

Option 5: Change the Port for Docker PostgreSQL

After running the command: pgcli -h localhost -p 5432 -u root -d ny_taxi User get the enter password prompt and despite using the correct one, the error persist. This is provably due to user having installed Postgres in local machine. The easiest solution to this port conflict between host and container is by Changing the Port for Docker PostgreSQL: You can configure your Docker PostgreSQL container to use a different port. This way, it won't conflict with the PostgreSQL instance running on your local machine. When running the PostgreSQL container, map it to a different port on your host machine. E.g.:

 docker run -it \\

-e POSTGRES_USER="root" \\

-e POSTGRES_PASSWORD="root" \\

-e POSTGRES_DB="ny_taxi" \\

-v c:/workspace/de-zoomcamp/1_intro_to_data_engineering/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \\

-p 5433:5432 \\

Postgres:13

5433 refers to the port on the host machine.

5432 refers to the port inside the Docker Postgres container.

