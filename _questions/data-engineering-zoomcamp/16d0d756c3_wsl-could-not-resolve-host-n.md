---
course: data-engineering-zoomcamp
id: 16d0d756c3
question: WSL - Could not resolve host name
section: 'Module 1: Docker and Terraform'
sort_order: 1050
---

Such as the issue above, WSL2 may not be referencing the correct .ssh/config path from Windows. You can create a config file at the home directory of WSL2.

cd ~

mkdir .ssh

Create a config file in this new .ssh/ folder referencing this folder:

HostName [GPC VM external IP]

User [username]

IdentityFile ~/.ssh/[private key]

