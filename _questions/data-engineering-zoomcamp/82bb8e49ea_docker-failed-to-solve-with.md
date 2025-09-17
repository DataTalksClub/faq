---
course: data-engineering-zoomcamp
id: 82bb8e49ea
question: 'Docker - failed to solve with frontend dockerfile.v0: failed to read dockerfile:
  error from sender: open ny_taxi_postgres_data: permission denied.'
section: 'Module 1: Docker and Terraform'
sort_order: 750
---

This happens on Ubuntu/Linux systems when trying to run the command to build the Docker container again.

$ docker build -t taxi_ingest:v001 .

A folder is created to host the Docker files. When the build command is executed again to rebuild the pipeline or create a new one the error is raised as there are no permissions on this new folder. Grant permissions by running this comtionmand;

$ sudo chmod -R 755 ny_taxi_postgres_data

Or use 777 if you still see problems. 755 grants write access to only the owner.

