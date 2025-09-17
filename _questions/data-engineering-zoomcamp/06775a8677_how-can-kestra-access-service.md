---
id: 06775a8677
question: How can Kestra access service account credential?
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1870
---

Do not directly add the content of service account credential json in Kestra script, especially if we are pushing to Github. Follow the instruction to add the service account as a secret .

When we need to use it in Kestra, we can pull it through {{ secret('GCP_SERVICE_ACCOUNT') }}

In the pluginDefaults.

