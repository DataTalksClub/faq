---
id: a25406395b
question: Subnetwork 'default' does not support Private Google Access which is required for Dataproc clusters when 'internal_ip_only' is set to 'true'. Enable Private Google Access on subnetwork 'default' or set 'internal_ip_only' to 'false'.
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3870
---

Search for VPC in Google Cloud Console

Navigate to the second tab “SUBNETS IN CURRENT PROJECT”

Look for the region/location where your dataproc will be located and click on it

Click the edit button and toggle on the button for “Private Google Access”

Save changes.

