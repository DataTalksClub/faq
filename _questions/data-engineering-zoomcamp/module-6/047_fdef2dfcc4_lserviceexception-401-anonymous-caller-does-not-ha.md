---
id: fdef2dfcc4
question: 'lServiceException: 401 Anonymous caller does not have storage.objects.list
  access to the Google Cloud Storage bucket. Permission ''storage.objects.list'' denied
  on resource (or it may not exist).'
sort_order: 47
---

This occurs because you are not logged in with Google Cloud SDK, or the project ID is not set. Follow these steps:

1. Log in using Google Cloud SDK:
   
   ```bash
   gcloud auth login
   ```
   
   This will open a tab in the browser. Accept the terms, then close the tab if needed.

2. Set the project ID:
   
   ```bash
   gcloud config set project <YOUR_PROJECT_ID>
   ```

3. Upload the `pq` directory to a Google Cloud Storage (GCS) Bucket:
   
   ```bash
   gsutil -m cp -r pq/ <YOUR_URI_from_gsutil>/pq
   ```