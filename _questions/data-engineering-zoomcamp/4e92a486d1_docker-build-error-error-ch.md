---
course: data-engineering-zoomcamp
id: 4e92a486d1
question: 'Docker - build error: error checking context: ''can''t stat ''/home/user/repos/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data''''.'
section: 'Module 1: Docker and Terraform'
sort_order: 720
---

This error appeared when running the command: docker build -t taxi_ingest:v001 .

When feeding the database with the data the user id of the directory ny_taxi_postgres_data was changed to 999, so my user couldn’t access it when running the above command. Even though this is not the problem here it helped to raise the error due to the permission issue.

Since at this point we only need the files Dockerfile and ingest_data.py, to fix this error one can run the docker build command on a different directory (having only these two files).

A more complete explanation can be found here:

You can fix the problem by changing the permission of the directory on ubuntu with following command:

sudo chown -R $USER dir_path

On windows follow the link:  

											Added by
											Kenan Arslanbay

