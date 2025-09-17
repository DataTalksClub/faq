---
course: data-engineering-zoomcamp
id: 5849afe5f6
question: 'stoTerraform - Error creating Bucket: googleapi: Error 403: Permission
  denied to access ‘storage.buckets.create’'
section: 'Module 1: Docker and Terraform'
sort_order: 1690
---

The error:

Error: googleapi: Error 403: terraform-trans-campus@trans-campus-410115.iam.gserviceaccount.com does not have storage.buckets.create access to the Google Cloud project. Permission 'storage.buckets.create' denied on resource (or it may not exist)., forbidden

The solution:

You have to declare the project name as your Project ID, and not your Project name, available on GCP console Dashboard.

