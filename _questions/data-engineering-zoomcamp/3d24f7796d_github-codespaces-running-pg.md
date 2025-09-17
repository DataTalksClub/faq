---
course: data-engineering-zoomcamp
id: 3d24f7796d
question: Github Codespaces - Running pgadmin in docker
section: 'Module 1: Docker and Terraform'
sort_order: 560
---

With the default instructions and running pgadmin in docker you may receive a blank screen after logging in to the pgadmin console. To resolve this, add the following two environment variables to your pgadmin config to allow it to work with codespace’s reverse proxy:

PGADMIN_CONFIG_PROXY_X_HOST_COUNT: 1
PGADMIN_CONFIG_PROXY_X_PREFIX_COUNT: 1

