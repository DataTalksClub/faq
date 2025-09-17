---
id: db53f69d74
question: 'Adding a pgadmin service with volume mounting to the docker-compose:'
sort_order: 1880
---

I encountered an error where the localhost url for pgadmin would just hang up (i chose localhost:8080 for my pgadmin, and made kestra localhost:8090, personal preference).

The associated error was:

And the resolution involved changing the ownership of my local directory to the user “5050” which is pgadmin. Unlike postgres, pgadmin requires you to give it permission. Apparently the postgres user inside the docker container creates the postgres volume/dir, so it has permission`s already.

This is a good source: [https://stackoverflow.com/questions/64781245/permission-denied-var-lib-pgadmin-sessions-in-docker](https://stackoverflow.com/questions/64781245/permission-denied-var-lib-pgadmin-sessions-in-docker)G

