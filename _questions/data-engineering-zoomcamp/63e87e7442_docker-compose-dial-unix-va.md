---
course: data-engineering-zoomcamp
id: 63e87e7442
question: 'Docker-Compose - dial unix /var/run/docker.sock: connect: permission denied'
section: 'Module 1: Docker and Terraform'
sort_order: 920
---

This happens if you did not create the docker group and added your user. Follow these steps from the link:

And then press ctrl+D to log-out and log-in again. pgAdmin: Maintain state so that it remembers your previous connection

If you are tired of having to setup your database connection each time that you fire up the containers, all you have to do is create a volume for pgAdmin:

In your docker-compose.yaml file, enter the following into your pgAdmin declaration:

volumes:

- type: volume

source: pgadmin_data

target: /var/lib/pgadmin

Also add the following to the end of the file:ls

volumes:

Pgadmin_data:

