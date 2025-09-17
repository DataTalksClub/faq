---
id: aeaede4fd1
question: How do I properly authenticate a Google Cloud Service Account in Kestra?
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1900
---

Several authentication methods are available;

These are some of the most straightforward approaches.

Method 1:

Update your docker-compose.yml file as follows:

Method 2:

Step 1: Store the Service Account as a Secret

Run this command, specifying the correct path to your service-account.json file and .env_encoded:

Modify docker-compose.yml to include the encoded secrets:

Step 2: Configure Kestra Plugin Defaults

This ensures all GCP tasks use the secret automatically:

Step 3: Verify it’s working in a testing GCP workflow

Additional - QA

Question: How do I update the Service Account key?

Answer: Generate a new key, re-run the Base64 command, and restart Kestra.

Question: Why use secrets instead of embedding the JSON key in the task?

Answer: Secrets prevent credential exposure and make workflows easier to manage.

Question: Can I apply this method to other GCP tasks?

Answer: Yes, all GCP plugins will automatically inherit the secret.

