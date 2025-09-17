---
id: 68f8a4b307
question: GCP VM -  connect to host port 22 no route to host
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1580
---

(reference: https://serverfault.com/questions/953290/google-compute-engine-ssh-connect-to-host-ip-port-22-operation-timed-out)Go to edit your VM.

Go to section Automation

Add Startup script
```
#!/bin/bash
sudo ufw allow ssh
```

Stop and Start VM.

