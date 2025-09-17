---
course: machine-learning-zoomcamp
id: 5d9aed1fd0
question: Save Docker Image to local machine and view contents
section: 9. Serverless Deep Learning
sort_order: 3260
---

The docker image can be saved/exported to tar format in local machine using the below command:

docker image save <image-name> -o <name-of-tar-file.tar>

The individual layers of the docker image for the filesystem content can be viewed by extracting the layer.tar present in the <name-of-tar-file.tar> created from above.

Sumeet Lalla

