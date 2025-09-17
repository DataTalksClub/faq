---
id: af5f29b64f
question: AWS EC2 instance constantly drops SSH connection
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 400
---

My SSH connection to AWS cannot last more than a few minutes, whether via terminal or VS code.

My config:

# Copy Configuration in local nano editor, then Save it!

Host mlops-zoomcamp                                         # ssh connection calling name

User ubuntu                                             # username AWS EC2

HostName <instance-public-IPv4-addr>                    # Public IP, it changes when Source EC2 is turned off.

IdentityFile ~/.ssh/name-of-your-private-key-file.pem   # Private SSH key file path

LocalForward 8888 localhost:8888                        # Connecting to a service on an internal network from the outside, static forward or set port user forward via on vscode

StrictHostKeyChecking no

Added by Muhammed Çelik

The disconnection will occur whether I SSH via WSL2 or via VS Code, and usually occurs after I run some code, i.e. “import mlflow”, so not particularly intense computation.

I cannot reconnect to the instance without stopping and restarting with a new IPv4 address.

I’ve gone through steps listed on this page:

Inbound rule should allow all incoming IPs for SSH.

What I expect to happen:

SSH connection should remain while I’m actively using the instance, and if it does disconnect, I should be able to reconnect back.

Solution: sometimes the hang ups are caused by the instance running out of memory. In one instance, using EC2 feature to view screenshot of the instance as a means to troubleshoot, it was the OS out-of-memory feature which killed off some critical processes. In this case, if we can’t use a higher compute VM with more RAM, try adding a swap file, which uses the disk as RAM substitute and prevents the OOM error. Follow Ubuntu’s documentation here: .

Alternatively follow AWS’s own doc, which mirrors Ubuntu’s:

Added by Claudia van Dijk: In addition, if your connection happens to be dropping because of timeouts, you can add this line to your local .ssh/config file, which makes it ping the connection every 50 seconds in case timeout is set to 60 seconds:

ServerAliveInterval 50

