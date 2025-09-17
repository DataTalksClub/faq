---
course: mlops-zoomcamp
id: b7625d600a
question: 'psycopg.OperationalError: connection failed: connection to server at "127.0.0.1",
  port 5432 failed: FATAL:  password authentication failed for user "postgres"'
section: 'Module 5: Monitoring'
sort_order: 2160
---

It could be that there is already a another docker container running (for example, from previous week).

Check with docker ps, and stop it with docker stop container_name_or_ID

Added Ibai Irastorza

