---
course: data-engineering-zoomcamp
id: 76f95c1d28
question: Terraform - Terraform initialized in an empty directory! The directory has
  no Terraform configuration files. You may begin working with Terraform immediately
  by creating Terraform configuration files.g
section: 'Module 1: Docker and Terraform'
sort_order: 1670
---

You get this error because I run the command terraform init outside the working directory, and this is wrong.You need first to navigate to the working directory that contains terraform configuration files, and then run the command.

