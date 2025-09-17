---
id: c670950570
question: My connection to my GCP VM instance keeps timing out when I try to connect
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 430
---

If you switched off the VM instance completely in GCP then when it switches back on the IP address changes. You need to update the ssh_config file with the new external IP address. This can be done in VS Code if you have the Remote-SSH extension installed. Open the command palette and type `Remote-SSH Open SSH Configuration File…` then select the appropriate ssh_config file. And edit the HostName to the correct IP address.

