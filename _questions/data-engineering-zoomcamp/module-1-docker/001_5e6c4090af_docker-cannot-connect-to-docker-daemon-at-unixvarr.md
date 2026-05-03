---
id: 5e6c4090af
question: 'Docker: Cannot connect to Docker daemon at unix:///var/run/docker.sock.
  Is the Docker daemon running?'
sort_order: 1
---

Make sure you're able to start the Docker daemon. Check the issue immediately as described below:

- Ensure the Docker daemon is running.
- Update WSL in PowerShell with the following command:

  ```bash
  wsl --update
  ```