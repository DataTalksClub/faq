---
id: bceb4aa421
question: Docker - docker pull dbpage
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 590
---

Whenever a `docker pull is performed (either manually or by `docker-compose up`), it attempts to fetch the given image name (pgadmin4, for the example above) from a repository (dbpage). 
IF the repository is public, the fetch and download happens without any issue whatsoever.

For instance:

docker pull postgres:13

docker pull dpage/pgadmin4

BE ADVISED:

The Docker Images we'll be using throughout the Data Engineering Zoomcamp are all public (except when or if explicitly said otherwise by the instructors or co-instructors).

Meaning: you are NOT required to perform a docker login to fetch them. 

So if you get the message above saying "docker login': denied: requested access to the resource is denied. That is most likely due to a typo in your image name:

For instance:

$ docker pull dbpage/pgadmin4

Will throw that exception telling you "repository does not exist or may require 'docker login'

Error response from daemon: pull access denied for dbpage/pgadmin4, repository does not exist or 
may require 'docker login': denied: requested access to the resource is denied

But that actually happened because the actual image is dpage/pgadmin4 and NOT dbpage/pgadmin4

How to fix it:

$ docker pull dpage/pgadmin4

EXTRA NOTES:
In the real world, occasionally, when you're working for a company or closed organisation, the Docker image you're trying to fetch might be under a private repo that your DockerHub Username was granted access to.

For which cases, you must first execute:
$ docker login

Fill in the details of your username and password.

And only then perform the `docker pull` against that private repository

