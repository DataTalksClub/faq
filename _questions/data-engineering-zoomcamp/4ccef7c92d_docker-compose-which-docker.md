---
course: data-engineering-zoomcamp
id: 4ccef7c92d
question: Docker-Compose - Which docker-compose binary to use for WSL?
section: 'Module 1: Docker and Terraform'
sort_order: 970
---

To figure out which docker-compose you need to download from [https://github.com/docker/compose/releases](https://github.com/docker/compose/releases) you can check your system with these commands:

uname -s  -> return Linux most likely

uname -m -> return "flavor"

Or try this command -

sudo curl -L "[GitHub](https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname) -s)-$(uname -m)" -o /usr/local/bin/docker-compose

