---
id: 0c9fc7e7d3
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_6ab99490.png
question: 'Error: Insufficient ''SSD_TOTAL_GB'' quota. Requested 500.0, available
  470.0.'
sort_order: 52
---

Sometimes while creating a dataproc cluster on GCP, the following error is encountered.

<{IMAGE:image_1}>

Solutions:

1. As mentioned [here](https://stackoverflow.com/a/59038704/22748533), sometimes there might not be enough resources in the given region to allocate the request. Usually, resources get freed up in a bit, and one can create a cluster.

2. Changing the type of boot-disk from PD-Balanced to PD-Standard in Terraform helped solve the problem.