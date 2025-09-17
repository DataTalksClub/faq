---
course: data-engineering-zoomcamp
id: a63d2734b2
question: GCP VM - VM connection request timeout
section: 'Module 1: Docker and Terraform'
sort_order: 1570
---

Question: I connected to my VM perfectly fine last week (ssh) but when I tried again this week, the connection request keeps timing out.

✅Answer: Start your VM. Once the VM is running, copy its External IP and paste that into your config file within the ~/.ssh folder.

cd ~/.ssh

code config ← this opens the config file in VSCode

