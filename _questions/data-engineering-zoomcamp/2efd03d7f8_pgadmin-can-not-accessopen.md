---
id: 2efd03d7f8
question: pgAdmin - Can not access/open the PgAdmin address via browser
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1270
---

I am using a Mac Pro device and connect to the GCP Compute Engine via Remote SSH - VSCode. But when I trying to run the PgAdmin container via docker run or docker compose command, I am failed to access the pgAdmin address via my browser. I have switched to another browser, but still can not access the pgAdmin address. So I modified a little bit the configuration from the previous DE Zoomcamp repository like below and can access the pgAdmin address:

Solution #1:

Modified “docker run” command

docker run --rm -it \

-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \

-e PGADMIN_DEFAULT_PASSWORD="pgadmin" \

-e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \

-e PGADMIN_LISTEN_ADDRESS=0.0.0.0 \

-e PGADMIN_LISTEN_PORT=5050 \

-p 5050:5050 \

--network=de-zoomcamp-network \

--name pgadmin-container \

--link postgres-container \

-t dpage/pgadmin4

Solution #2:

Modified docker-compose.yaml configuration (via “docker compose up” command)

pgadmin:

image: dpage/pgadmin4

container_name: pgadmin-conntainer

environment:

- PGADMIN_DEFAULT_EMAIL=admin@admin.com

- PGADMIN_DEFAULT_PASSWORD=pgadmin

- PGADMIN_CONFIG_WTF_CSRF_ENABLED=False

- PGADMIN_LISTEN_ADDRESS=0.0.0.0

- PGADMIN_LISTEN_PORT=5050

volumes:

- "./pgadmin_data:/var/lib/pgadmin/data"

ports:

- "5050:5050"

networks:

- de-zoomcamp-network

depends_on:

- postgres-conntainer

