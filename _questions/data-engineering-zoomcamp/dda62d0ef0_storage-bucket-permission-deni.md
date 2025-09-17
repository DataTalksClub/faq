---
id: dda62d0ef0
question: Storage Bucket Permission Denied Error when running the gcp_setup flow
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1880
---

When following the  and then running the , I get the following error:

I tried manually creating the bucket in the GCP console, but this showed me that the bucket already existed. So I came up with another name for the bucket and it worked.

The GCP bucket name has to be unique globally across all buckets, even if those are not your buckets, because the bucket will be accessible by URL.

