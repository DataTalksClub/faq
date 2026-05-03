---
id: 733065c175
question: Why does Kestra need access to the Docker socket?
sort_order: 20
---

Kestra runs many tasks inside Docker containers, and Kestra itself is responsible for starting those containers when needed. To do this, Kestra needs access to the host Docker daemon, which is exposed via the Docker socket at /var/run/docker.sock. In the official Docker Compose setup for Kestra, the container runs as root and mounts /var/run/docker.sock:/var/run/docker.sock, because the Docker Compose implementation requires root privileges to access the socket. This configuration is intended for development purposes.