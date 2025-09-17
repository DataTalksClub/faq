---
id: 87e92edf02
question: Docker - ny_taxi_postgres_data is empty
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 660
---

Even after properly running the docker script the folder is empty in the vs code  then try this (For Windows)

winpty docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v "C:\Users\abhin\dataengg\DE_Project_git_connected\DE_OLD\week1_set_up\docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data" \

-p 5432:5432 \

postgres:13

Here quoting the absolute path in  the -v parameter is solving the issue and all the files are visible in the Vs-code ny_taxi folder as shown in the video.

Note: Check he example for the direction of the / \

**Another possible solution for windows, make sure to finish the folder path with a forward slash / :

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v /"$(pwd)"/ny_taxi_postgres_data/:/var/lib/postgresql/data/\

-p 5432:5432 \

postgres:13

