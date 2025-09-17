---
course: data-engineering-zoomcamp
id: 3124f13c7c
question: 'pgAdmin - Unable to connect to server: [Errno -3] Try again'
section: 'Module 1: Docker and Terraform'
sort_order: 1290
---

This error occurs in connecting pgAdmin with Docker Postgres. In tutorial, in the pgAdmin server creation under Connection > Host name/address: pg-database is given and resulted in the above mentioned error when saved.

Solution 1:

Verify that both containers are connected to pg-network : docker network inspect pg-network

If Docker Postgres container is not connected, then connect it to pg-network: docker network connect pg-network postgresContainer_name

Retry connection, and if error persist, instead of using pg-database under Connection > Host name/address: pg-database, Try using IP Address: Use the IP address of the postgresContainer_name container e.g.(172.19.0.3) in the pgAdmin configuration instead of the container name or pg-database.

