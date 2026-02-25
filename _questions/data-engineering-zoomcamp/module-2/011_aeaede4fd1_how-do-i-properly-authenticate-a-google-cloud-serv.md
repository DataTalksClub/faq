---
id: aeaede4fd1
question: How do I properly authenticate a Google Cloud Service Account in Kestra?
sort_order: 11
---

Several authentication methods are available; here are some of the most straightforward approaches:

### Method 1:

Update your `docker-compose.yml` file as needed.

### Method 2:

1. **Store the Service Account as a Secret**  
   Run this command, specifying the correct path to your `service-account.json` file and `.env_encoded`:

   ```bash
   # Example command: Adjust according to your environment
   base64 /path/to/service-account.json > .env_encoded
   ```

2. **Modify `docker-compose.yml` to Include the Encoded Secrets**  
   Insert the relevant configuration within your `docker-compose.yml`.

3. **Configure Kestra Plugin Defaults**  
   This ensures all GCP tasks use the secret automatically.

4. **Verify it’s Working in a Testing GCP Workflow**

See also related FAQs on updating the service account key, using secrets, and applying this method to other GCP tasks.