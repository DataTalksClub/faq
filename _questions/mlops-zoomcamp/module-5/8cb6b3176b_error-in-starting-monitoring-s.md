---
id: 8cb6b3176b
question: Error in starting monitoring services in Linux
sort_order: 1940
---

Problem Description : In Linux, when starting services using docker compose up --build  as shown in video 5.2, the services won’t start and instead we get message unknown flag: --build in command prompt.

Solution : Since we install docker-compose separately in Linux, we have to run docker-compose up --build instead of docker compose up --build

Added by Ashish Lalchandani

