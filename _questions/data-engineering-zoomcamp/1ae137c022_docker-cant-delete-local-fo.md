---
course: data-engineering-zoomcamp
id: 1ae137c022
question: Docker - can’t delete local folder that mounted to docker volume
section: 'Module 1: Docker and Terraform'
sort_order: 610
---

When I runned command to create postgre in docker container it created folder on my local machine to mount it to volume inside container. It has write and read protection and owned by user 999, so I could not delete it by simply drag to trash.  My obsidian could not started due to access error, so I had to change placement of this folder and delete old folder by this command:

sudo rm -r -f docker_test/

- where `rm` - remove, `-r` - recursively, `-f` - force, `docker_test/` - folder.

