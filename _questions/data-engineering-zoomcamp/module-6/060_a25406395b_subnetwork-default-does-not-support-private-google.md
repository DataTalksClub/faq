---
id: a25406395b
question: Subnetwork 'default' does not support Private Google Access which is required
  for Dataproc clusters when 'internal_ip_only' is set to 'true'. Enable Private Google
  Access on subnetwork 'default' or set 'internal_ip_only' to 'false'.
sort_order: 60
---

To resolve this issue, follow these steps:

1. Search for VPC in Google Cloud Console.
2. Navigate to the "SUBNETS IN CURRENT PROJECT" tab.
3. Locate the region/location where your Dataproc will be located and click on it.
4. Click the edit button and toggle on "Private Google Access."
5. Save changes.