---
id: 5d66421473
question: taskid: yellow_create_table The connection attempt failed. Host.docker.internal
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1930
---

If you're using Linux, you might encounter Connection Refused errors when connecting to the Postgres DB from within Kestra. This is because host.docker.internal works differently on Linux.

Using the modified Docker Compose file in 02-workflow-orchestration readme troubleshooting tips Docker Compose Example, you can run both Kestra and its dedicated Postgres DB, as well as the Postgres DB for the exercises all together. You can access it within Kestra by referring to the container name postgres_zoomcamp instead of host.docker.internal in pluginDefaults.

The pluginDefaults exist in both 2_postgres_taxi_scheduled.yaml, 02_postgres_taxi.yaml, please modify as shown below.

![Image](images/data-engineering-zoomcamp/image_e66c0b8d.png)

