---
course: mlops-zoomcamp
id: 560c0eb368
question: Managing Multiple Docker Containers with docker-compose profile
section: 'Module 6: Best practices'
sort_order: 2330
---

Problem description

When a docker-compose file contains a lot of containers, running the containers may take too much resource. There is a need to easily select only a group of containers while ignoring irrelevant containers during testing.

Solution description

Add profiles: [“profile_name”] in the service definition.

When starting up the service, add `--profile profile_name` in the command.

Added by Ammar Chalifah

