---
id: 51bc7e280d
question: GCP VM - mkdir: cannot create directory ‘.ssh’: Permission denied
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1550
---

I am trying to create a directory but it won't let me do it

User1@DESKTOP-PD6UM8A MINGW64 /

$ mkdir .ssh

mkdir: cannot create directory ‘.ssh’: Permission denied

You should do it in your home directory. Should be your home (~)

Local. But it seems you're trying to do it in the root folder (/). Should be your home (~)

