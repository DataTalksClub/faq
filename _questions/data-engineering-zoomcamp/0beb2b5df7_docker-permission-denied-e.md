---
course: data-engineering-zoomcamp
id: 0beb2b5df7
question: Docker - "permission denied" error when creating a PostgreSQL Docker with
  a mounted volume on macOS M1
section: 'Module 1: Docker and Terraform'
sort_order: 600
---

Issue Description:

When attempting to run a Docker command similar to the one below:

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \

-p 5432:5432 \mount

postgres:13

You encounter the error message:

docker: Error response from daemon: error while creating mount source path '/path/to/ny_taxi_postgres_data': chown /path/to/ny_taxi_postgres_data: permission denied.

Solution:

1- Stop Rancher Desktop:

If you are using Rancher Desktop and face this issue, stop Rancher Desktop to resolve compatibility problems.

2- Install Docker Desktop:

Install Docker Desktop, ensuring that it is properly configured and has the required permissions.

2-Retry Docker Command:

Run the Docker command again after switching to Docker Desktop. This step resolves compatibility issues on some systems.

Note: The issue occurred because Rancher Desktop was in use. Switching to Docker Desktop resolves compatibility problems and allows for the successful creation of PostgreSQL containers with mounted volumes for the New York Taxi Database on macOS M1.

