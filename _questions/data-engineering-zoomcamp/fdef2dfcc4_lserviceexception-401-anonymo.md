---
id: fdef2dfcc4
question: lServiceException: 401 Anonymous caller does not have storage.objects.list access to the Google Cloud Storage bucket. Permission 'storage.objects.list' denied on resource (or it may not exist).
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3740
---

This occurs because you are not logged in “gcloud auth login” and maybe the project id is not settled. Then type in a terminal:

gcloud auth login

This will open a tab in the browser, accept the terms, after that close the tab if you want. Then set the project is like:

gcloud config set project <YOUR PROJECT_ID>

Then you can run the command to upload the pq dir to a GCS Bucket:

gsutil -m cp -r pq/ <YOUR URI from gsutil>/pq

