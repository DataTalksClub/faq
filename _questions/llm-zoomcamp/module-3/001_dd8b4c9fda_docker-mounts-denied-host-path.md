---
id: dd8b4c9fda
question: 'How do I fix the Docker error ''mounts denied: The path /tmp/... is not
  shared from the host''?'
sort_order: 1
---

Add the path to Docker File Sharing (Recommended)
You need to explicitly tell Docker Desktop that it is allowed to access your host's /tmp directory.
1. Open Docker Desktop.
2. Click the Gear icon (Settings) in the top right corner.
3. Navigate to Resources > File Sharing.
4. Click the + (Add) button.
5. Enter /tmp (or the specific path like /tmp/kestra-wd) and press Enter.
6. Click Apply & restart.

Once the changes are applied, go to the terminal and rerun the docker compose command (docker compose up -d) to stand up Kestra