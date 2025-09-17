---
course: data-engineering-zoomcamp
id: 8ddf54cbd0
question: PGCLI - should we run pgcli inside another docker container?
section: 'Module 1: Docker and Terraform'
sort_order: 1070
---

In this section of the course, the 5432 port of pgsql is mapped to your computer’s 5432 port. Which means you can access the postgres database via pgcli directly from your computer.

So No, you don’t need to run it inside another container. Your local system will do.

