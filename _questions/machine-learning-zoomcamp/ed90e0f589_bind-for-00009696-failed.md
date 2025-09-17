---
course: machine-learning-zoomcamp
id: ed90e0f589
question: 'Bind for 0.0.0.0:9696 failed: port is already allocated'
section: 5. Deploying Machine Learning Models
sort_order: 2060
---

I was getting the below error when I rebuilt the docker image although the port was not allocated, and it was working fine.

Error message:

Error response from daemon: driver failed programming external connectivity on endpoint beautiful_tharp (875be95c7027cebb853a62fc4463d46e23df99e0175be73641269c3d180f7796): Bind for 0.0.0.0:9696 failed: port is already allocated.

Solution description

Issue has been resolved running the following command:

docker kill $(docker ps -q)

Asia Saeed

