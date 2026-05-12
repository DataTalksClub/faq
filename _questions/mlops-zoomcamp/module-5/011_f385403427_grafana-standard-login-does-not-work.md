---
id: f385403427
question: 'Grafana: Standard login does not work'
sort_order: 11
---

When trying to log in to Grafana with the standard credentials (admin/admin), an error occurs.

1. To reset the admin password, use the following command inside the Grafana container:

   ```bash
   grafana cli admin reset-admin-password admin
   ```

   **Note:** The `grafana-cli` command is deprecated. Use `grafana cli` instead.

2. Enter the Docker container with Grafana:

   - Find the Container ID by running:
     
     ```bash
     docker ps
     ```

   - Use the Container ID to reset the password. Replace `<container_ID>` with the actual Container ID:

     ```bash
     lpep_pickup_datetime<container_ID> grafana cli admin reset-admin-password admin
     ```

This should resolve the login issue.