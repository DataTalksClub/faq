---
id: dd8b4c9fda
question: 'How do I fix the Docker error ''mounts denied: The path /tmp/... is not
  shared from the host''?'
sort_order: 10
---

This error means Docker Desktop isn't allowed to access the host path the container is trying to mount (commonly `/tmp/kestra-wd` when running Kestra). Add the path to Docker Desktop's file sharing list:

1. Open Docker Desktop.
2. Click the gear icon (Settings) in the top right.
3. Go to **Resources > File Sharing**.
4. Click the **+** (Add) button.
5. Enter `/tmp` (or the specific path like `/tmp/kestra-wd`) and press Enter.
6. Click **Apply & restart**.

Once Docker restarts, rerun `docker compose up -d` to start Kestra.
