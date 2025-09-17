---
id: 9abc27b002
question: Kestra: Don’t forget to set GCP_CREDS variable
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1960
---

If you plan on using Kestra with Google Cloud Platform, make sure you setup the GCP_CREDS that’s gonna be used in the flows that has “gcp” on its name.

To set it, go to Namespaces, and then select “zoomcamp” if you are using the same examples used in the lessons. Then in the “KV Store” tab create the new key as GCP_CREDS and set the type to JSON and paste the content of the .json file with credentials for the service account created.

