---
id: 7c4d422363
question: Docker - build error checking context: can’t stat ‘/home/fhrzn/Projects/…./ny_taxi_postgres_data’
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 740
---

Found the issue in the PopOS linux. It happened because our user didn’t have authorization rights to the host folder ( which also caused folder seems empty, but it didn’t!).

✅Solution:

Just add permission for everyone to th

777 <path_to_folder>

Example:

sudo chmod -R 777 ny_taxi_postgres_data/

