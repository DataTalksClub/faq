---
course: data-engineering-zoomcamp
id: c1eeebf4ce
question: 'Docker - Error response from daemon: error while creating buildmount source
  path ''/run/desktop/mnt/host/c/<your path>'': mkdir /run/desktop/mnt/host/c: file
  exists'
section: 'Module 1: Docker and Terraform'
sort_order: 710
---

When you run this command second time

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-v <your path>:/var/lib/postgresql/data \

-p 5432:5432 \

postgres:13

The error message above could happen. That means you should not mount on the second run. This command helped me:

When you run this command second time

docker run -it \

-e POSTGRES_USER="root" \

-e POSTGRES_PASSWORD="root" \

-e POSTGRES_DB="ny_taxi" \

-p 5432:5432 \

postgres:13

