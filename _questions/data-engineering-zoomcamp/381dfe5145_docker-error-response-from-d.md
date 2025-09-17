---
id: 381dfe5145
question: Docker - Error response from daemon: Conflict. The container name "pg-database" is already in use by container “xxx”.  You have to remove (or rename) that container to be able to reuse that name.
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 770
---

Sometimes, when you try to restart a docker image configured with a network name, the above message appears. In this case, use the following command with the appropriate container name:
>>> If the container is running state, use docker stop <container_name>
>>> then, docker rm pg-database
Or use docker start instead of docker run in order to restart the docker image without removing it.

