---
id: bd56924fcb
question: 'GCP: Static vs Ephemeral IP / Setting up static IP for VM'
sort_order: 1
---

When you set up a VM in Google Cloud Platform (GCP), it initially uses an ephemeral IP address, which changes each time you start or stop the VM. If you need a consistent IP for your configuration file, you should set up a static IP address.

### Steps to Set Up a Static IP Address

1. Navigate to **VPC Network** > **IP addresses** in the GCP console.
2. Allocate a new static IP address.
3. Attach the static IP to your VM instance.

> **Note:** You are charged for a static IP if it is not allocated to a specific VM, so make sure it is attached to avoid extra fees.

For detailed instructions, consult the [GCP documentation](https://cloud.google.com/).