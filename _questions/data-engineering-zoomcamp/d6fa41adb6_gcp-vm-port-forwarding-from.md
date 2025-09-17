---
id: d6fa41adb6
question: GCP VM - Port forwarding from GCP without using VS Code
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1590
---

You can easily forward the ports of pgAdmin, postgres and Jupyter Notebook using the built-in tools in Ubuntu and without any additional client:

First, in the VM machine, launch docker-compose up -d and jupyter notebook in the correct folder.

From the local machine, execute: ssh -i ~/.ssh/gcp -L 5432:localhost:5432 username@external_ip_of_vm

Execute the same command but with ports 8080 and 8888.

Now you can access pgAdmin on local machine in browser typing localhost:8080

For Jupyter Notebook, type localhost:8888 in the browser of your local machine. If you have problems with the credentials, it is possible that you have to copy the link with the access token provided in the logs of the terminal of the VM machine when you launched the jupyter notebook command.

To forward both pgAdmin and postgres use, ssh -i ~/.ssh/gcp -L 5432:localhost:5432 -L 8080:localhost:8080 modito@35.197.218.128

