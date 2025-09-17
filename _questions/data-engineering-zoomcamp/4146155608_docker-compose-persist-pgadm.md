---
course: data-engineering-zoomcamp
id: '4146155608'
question: Docker-Compose - Persist PGAdmin configuration
section: 'Module 1: Docker and Terraform'
sort_order: 910
---

As per the lessons,

Persisting pgAdmin configuration (i.e. server name) is done by adding a “volumes” section:

services:

pgdatabase:

[...]

pgadmin:

image: dpage/pgadmin4

environment:

- PGADMIN_DEFAULT_EMAIL=admin@admin.com

- PGADMIN_DEFAULT_PASSWORD=root

volumes:

- "./pgAdmin_data:/var/lib/pgadmin/sessions:rw"

ports:

- "8080:80"

In the example above, ”pgAdmin_data” is a folder on the host machine, and “/var/lib/pgadmin/sessions” is the session settings folder in the pgAdmin container.

Before running docker-compose up on the YAML file, we also need to give the pgAdmin container access to write to the “pgAdmin_data” folder. The container runs with a username called “5050” and user group “5050”. The bash command to give access over the mounted volume is:

sudo chown -R 5050:5050 pgAdmin_data

