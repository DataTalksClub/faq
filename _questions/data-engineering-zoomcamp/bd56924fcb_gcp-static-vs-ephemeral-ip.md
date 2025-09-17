---
course: data-engineering-zoomcamp
id: bd56924fcb
question: GCP - Static vs Ephemeral IP / Setting up static IP for VM
section: 'Module 1: Docker and Terraform'
sort_order: 1410
---

I had my contig file set up from the first instance of my VM setup, but once I shut the VM down and restarted it later, the config no longer worked. This was because the IP address of my VM had changed, so my config was out of date. I didn’t want to change my config file every time so I wondered if there was a solution – there is!

You can make a static IP address. The default is ephemeral, which changes every time you start/stop. This way, you can keep the same ip address in your config file every time you start/stop the VM.

Set up a static IP in VPC Network > IP addresses. Make sure you attach it to your VM instance to avoid extra fees. You are only charged for a static IP if it is not assigned to a specific virtual machine. There is also pretty good documentation for this on gcp.

