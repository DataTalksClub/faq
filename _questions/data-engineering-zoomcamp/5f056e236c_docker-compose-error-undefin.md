---
id: 5f056e236c
question: Docker-Compose - Error undefined volume in Windows/WSL
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 980
---

If you wrote the docker-compose.yaml file exactly like the video, you might run into an error like this:dev

service "pgdatabase" refers to undefined volume dtc_postgres_volume_local: invalid compose project

In order to make it work, you need to include the volume in your docker-compose file. Just add the following:

volumes:

dtc_postgres_volume_local:

