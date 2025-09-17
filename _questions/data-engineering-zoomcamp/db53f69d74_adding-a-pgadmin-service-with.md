---
id: db53f69d74
question: Adding a pgadmin service with volume mounting to the docker-compose:
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1850
---

I encountered an error where the localhost url for pgadmin would just hang up (i chose localhost:8080 for my pgadmin, and made kestra localhost:8090, personal preference).

The associated error was:

And the resolution involved changing the ownership of my local directory to the user “5050” which is pgadmin. Unlike postgres, pgadmin requires you to give it permission. Apparently the postgres user inside the docker container creates the postgres volume/dir, so it has permission`s already.

This is a good source: G

