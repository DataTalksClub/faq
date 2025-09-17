---
course: data-engineering-zoomcamp
id: 0cfd7f7ed6
question: pgAdmin - Blank/white screen after login (browser)
section: 'Module 1: Docker and Terraform'
sort_order: 1260
---

Using GitHub Codespaces in the browser resulted in a blank screen after the login to pgAdmin (running in a Docker container). The terminal of the pgAdmin container was showing the following error message:

CSRFError: 400 Bad Request: The referrer does not match the host.

Solution #1:

As recommended in the following issue   setting the following environment variable solved it.

PGADMIN_CONFIG_WTF_CSRF_ENABLED="False"

Modified “docker run” command

docker run --rm -it \

-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \

-e PGADMIN_DEFAULT_PASSWORD="root" \

-e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \

-p "8080:80" \

--name pgadmin \

--network=pg-network \

dpage/pgadmin4:8.2

Solution #2:

Using the local installed VSCode to display GitHub Codespaces.

When using GitHub Codespaces in the locally installed VSCode (opening a Codespace or creating/starting one) this issue did not occur.

