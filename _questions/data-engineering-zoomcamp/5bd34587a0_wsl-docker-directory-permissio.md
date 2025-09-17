---
course: data-engineering-zoomcamp
id: 5bd34587a0
question: WSL Docker directory permissions error
section: 'Module 1: Docker and Terraform'
sort_order: 1010
---

Error:  initdb: error: could not change permissions of directory

Issue: WSL and Windows do not manage permissions in the same way causing conflict if using the Windows file system rather than the WSL file system.

Solution: Use Docker volumes.

Why: Volume is used for storage of persistent data and not for use of transferring files. A local volume is unnecessary.

Benefit: This resolves permission issues and allows for better management of volumes.

NOTE: the ‘user:’ is not necessary if using docker volumes, but is if using local drive.

</>  docker-compose.yaml

services:

postgres:

image: postgres:15-alpine

container_name: postgres

user: "0:0"

environment:

- POSTGRES_USER=postgres

- POSTGRES_PASSWORD=postgres

- POSTGRES_DB=ny_taxi

volumes:

- "pg-data:/var/lib/postgresql/data"

ports:

- "5432:5432"

networks:

- pg-network

pgadmin:

image: dpage/pgadmin4

container_name: pgadmin

user: "${UID}:${GID}"

environment:

- PGADMIN_DEFAULT_EMAIL=email@some-site.com

- PGADMIN_DEFAULT_PASSWORD=pgadmin

volumes:

- "pg-admin:/var/lib/pgadmin"

ports:

- "8080:80"

networks:

- pg-network

networks:

pg-network:

name: pg-network

volumesta:

name: ingest_pgdata

pg-admin:

name: ingest_pgadmin:

pg-da

