---
id: db53f69d74
question: 'Adding a pgadmin service with volume mounting to the docker-compose:'
sort_order: 5
---

I encountered an error where the localhost URL for pgAdmin would just hang (I chose `localhost:8080` for my pgAdmin, and made kestra `localhost:8090`, personal preference).

The associated issue involved permissions. The resolution was to change the ownership of my local directory to the user "5050," which is pgAdmin. Unlike Postgres, pgAdmin requires explicit permission. Apparently, the Postgres user inside the Docker container creates the Postgres volume/dir, so it has permissions already.

This is a useful resource:

[Stack Overflow: Permission denied /var/lib/pgadmin/sessions in Docker](https://stackoverflow.com/questions/64781245/permission-denied-var-lib-pgadmin-sessions-in-docker)