---
course: data-engineering-zoomcamp
id: 3f1c2f93bd
question: Docker-Compose - mounting error
section: 'Module 1: Docker and Terraform'
sort_order: 840
---

error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted  volume

if you have used the prev answer (just before this) and have created a local docker volume, then you need to tell the compose file about the named volume:

volumes:

dtc_postgres_volume_local:  # Define the named volume here

# services mentioned in the compose file auto become part of the same network!

services:

your remaining code here . . .

now use docker volume inspect dtc_postgres_volume_local to see the location by checking the value of Mountpoint

In my case, after i ran docker compose up the mounting dir created was named ‘docker_sql_dtc_postgres_volume_local’ whereas it should have used the already existing ‘dtc_postgres_volume_local’

All i did to fix this is that I renamed the existing ‘dtc_postgres_volume_local’ to ‘docker_sql_dtc_postgres_volume_local’ and removed the newly created one (just be careful when doing this)

run docker compose up again and check if the table is there or not!

