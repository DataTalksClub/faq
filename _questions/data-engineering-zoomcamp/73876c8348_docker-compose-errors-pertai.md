---
course: data-engineering-zoomcamp
id: 73876c8348
question: Docker-Compose - Errors pertaining to docker-compose.yml and pgadmin setup
section: 'Module 1: Docker and Terraform'
sort_order: 950
---

For everyone who's having problem with Docker compose, getting the data in postgres and similar issues, please take care of the following:

create a new volume on docker (either using the command line or docker desktop app)

make the following changes to your docker-compose.yml file (see attachment)

set low_memory=false when importing the csv file (df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=1000, low_memory=False))

use the below function (in the upload-data.ipynb) for better tracking of your ingestion process (see attachment)

![Image](images/data-engineering-zoomcamp/image_63f6a6fb.png)

Order of execution:

(1) open terminal in 2_docker_sql folder and run docker compose up

(2) ensure no other containers are running except the one you just executed (pgadmin and pgdatabase)

(3) open jupyter notebook and begin the data ingestion

(4) open pgadmin and set up a server (make sure you use the same configurations as your docker-compose.yml file like the same name (pgdatabase), port, databasename (ny_taxi) etc.

