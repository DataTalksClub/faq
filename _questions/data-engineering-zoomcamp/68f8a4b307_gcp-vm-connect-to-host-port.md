---
course: data-engineering-zoomcamp
id: 68f8a4b307
question: GCP VM -  connect to host port 22 no route to host
section: 'Module 1: Docker and Terraform'
sort_order: 1580
---

(reference: [serverfault.com](https://serverfault.com/questions/953290/google-compute-engine-ssh-connect-to-host-ip-port-22-operation-timed-ou)t)Go to edit your VM.

Go to section Automation

Add Startup script```#!/bin/bashsudo ufw allow ssh```

Stop and Start VM.

