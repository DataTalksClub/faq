---
id: 381dfe5145
question: 'Docker: Error response from daemon: Conflict. The container name "pg-database"
  is already in use by container "xxx". You have to remove (or rename) that container
  to be able to reuse that name.'
sort_order: 14
---

Sometimes, when you try to restart a Docker container configured with a network name, the error message appears.

To resolve this issue:

1. If the container is in a running state, stop it using:
   
   ```bash
   docker stop <container_name>
   ```
   
2. Then remove the container:
   
   ```bash
   docker rm pg-database
   ```

Alternatively, you can use `docker start` instead of `docker run` to restart the Docker container without removing it.