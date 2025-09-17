---
course: machine-learning-zoomcamp
id: acdd201a06
question: Dumping/Retrieving only the size of for a specific Docker image
section: 5. Deploying Machine Learning Models
sort_order: 1920
---

Using the command docker images or docker image ls will dump all information for all local Docker images. It is possible to dump the information only for a specified image by using:

docker image ls <image name>

Or alternatively:

docker images <image name>

In action to that it is possible to only dump specific information provided using the option --format which will dump only the size for the specified image name when using the command below:

docker image ls --format "{{.Size}}" <image name>

Or alternatively:

docker images --format "{{.Size}}" <image name>

Sylvia Schmitt

