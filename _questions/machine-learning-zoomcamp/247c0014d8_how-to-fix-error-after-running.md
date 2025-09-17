---
course: machine-learning-zoomcamp
id: 247c0014d8
question: How to fix error after running the Docker run command
section: 5. Deploying Machine Learning Models
sort_order: 2050
---

![Image](images/machine-learning-zoomcamp/image_46ecce14.png)

Solution

This error was because there was another instance of gunicorn running. So I thought of removing this along with the zoomcamp_test image. However, it didn’t let me remove the orphan container. So I did the following

Running the following commands

docker ps -a <to list all docker containers>

docker images <to list images>

docker stop <container ID>

docker rm <container ID>

docker rmi image

I rebuilt the Docker image, and ran it once again; this time it worked correctly and I was able to serve the test script to the endpoint.

