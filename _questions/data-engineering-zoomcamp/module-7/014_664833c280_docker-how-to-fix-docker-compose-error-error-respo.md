---
id: 664833c280
question: 'Docker: How to fix docker compose error: Error response from daemon: pull
  access denied for spark-3.3.1, repository does not exist or may require ''docker
  login'': denied: requested access to the resource is denied'
sort_order: 14
---

If you get this error, it means you have not built your Spark and Jupyter images. These images aren’t readily available on DockerHub.

To resolve this:

- In the Spark folder, run the following command from a bash CLI to build all images before running docker compose:
  
  ```bash
  ./build.sh
  ```