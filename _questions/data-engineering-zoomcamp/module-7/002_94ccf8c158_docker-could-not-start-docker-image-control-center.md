---
id: 94ccf8c158
question: 'Docker: Could not start docker image "control-center" from the docker-compose.yaml
  file.'
sort_order: 2
---

Check Docker Compose File:

Ensure that your `docker-compose.yaml` file is correctly configured with the necessary details for the "control-center" service. Check the service name, image name, ports, volumes, environment variables, and any other configurations required for the container to start.

On Mac OSX 12.2.1 (Monterey), if you encounter this issue, try the following:

- Open Docker Desktop and check for any images still running from previous sessions.
- If there are images still running and they do not appear with the `docker ps` command, they may need to be deleted directly from Docker Desktop.
- Once those images are removed, try starting the Kafka environment again.

This approach resolved the issue on Mac OSX 12.2.1 for a similar setup.