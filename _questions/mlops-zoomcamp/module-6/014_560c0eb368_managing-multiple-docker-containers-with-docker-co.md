---
id: 560c0eb368
question: Managing Multiple Docker Containers with docker-compose profile
sort_order: 14
---

When a Docker Compose file contains many containers, running them all may consume too many resources. There is often a need to easily select only a group of containers while ignoring irrelevant ones during testing.

1. Add `profiles: ["profile_name"]` in the service definition within your `docker-compose.yml` file.

2. Start the service with the specific profile using the command:

   ```bash
   docker-compose --profile profile_name up
   ```