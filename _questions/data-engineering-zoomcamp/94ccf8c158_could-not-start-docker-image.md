---
course: data-engineering-zoomcamp
id: 94ccf8c158
question: Could not start docker image “control-center” from the docker-compose.yaml
  file.
section: 'Module 6: streaming with kafka'
sort_order: 3890
---

Check Docker Compose File:

Ensure that your docker-compose.yaml file is correctly configured with the necessary details for the "control-center" service. Check the service name, image name, ports, volumes, environment variables, and any other configurations required for the container to start.

On Mac OSX 12.2.1 (Monterey) I could not start the kafka control center. I opened Docker Desktop and saw docker images still running from week 4, which I did not see when I typed “docker ps.” I deleted them in docker desktop and then had no problem starting up the kafka environment.

