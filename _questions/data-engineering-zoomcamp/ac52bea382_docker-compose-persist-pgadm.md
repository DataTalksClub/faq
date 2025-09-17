---
id: ac52bea382
question: Docker-Compose - Persist PGAdmin docker contents on GCP
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 890
---

So one common issue is when you run docker-compose on GCP, postgres won’t persist it’s data to mentioned path for example:

services:

…

…

pgadmin:

…

…

Volumes:

“./pgadmin”:/var/lib/pgadmin:wr”

Might not work so in this use you can use Docker Volume to make it persist, by simply changing

services:

…

….

pgadmin:

…

…

Volumes:

pgadmin:/var/lib/pgadmin

volumes:

Pgadmin:

