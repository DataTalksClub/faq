---
id: 3fd406c55c
question: SSH Connection to AWS EC2 instance from local machine WSL getting terminated frequently within a minute of inactivity.
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 990
---

If the ssh connection from your local machine’s WSL to AWS EC2 instance is frequently getting terminated with very short span of inactivity with the following message displayed at prompt:

![Image](images/mlops-zoomcamp/image_e822dac8.png)

You can fix the same by adding the following lines to your config file at your .ssh directory in your WSL environment:

ServerAliveInterval 60

ServerAliveCountMax 3

For eg (for clarity). after adding these lines your ssh connection should look somewhat like this below:

Host mlops-zoomcamp

HostName 45.80.32.7

User ubuntu

IdentityFile ~/.ssh/siddMLOps.pem

StrictHostKeyChecking no

ServerAliveInterval 60

ServerAliveCountMax 3

Added by Siddhartha Gogoi

