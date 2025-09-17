---
id: 2acc8ec64a
question: How do I debug a docker container?
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1940
---

Launch the container image in interactive mode and overriding the entrypoint, so that it starts a bash command.

docker run -it --entrypoint bash <image>

If the container is already running, execute a command in the specific container:

docker ps (find the container-id)

docker exec -it <container-id> bash

(Marcos MJD)

