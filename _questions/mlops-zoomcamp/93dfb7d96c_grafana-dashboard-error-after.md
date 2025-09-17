---
id: 93dfb7d96c
question: Grafana dashboard error after reset: db query error: pq: database “test” does not exist
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2120
---

Problem: You’ve already loaded your data, created a dashboard and even saved it according to the exercise. But suddenly when you run docker-compose up after saving the dashboard file you get this error: db query error: pq: database “test” does not exist

![Image](images/mlops-zoomcamp/image_03216ab8.png)

Solution:

This error indicates you haven’t run the DB initialization code. But if you did run it before and even saw results, the most likely reason for the error is that you restarted the docker-compose services.

The default docker-compose.yml file doesn’t have a volume for the Postgres DB, so every restart will also delete the DB data with it.

If you’re not planning to restart the services again, the easiest solution would be to run the DB initialization and filling code of your exercise again and forget about this.

On the other hand, if you’ll run more services restarts, consider adding a volume to your postgres service in the docker-compose.yml file, e.g.:

volumes:

- ./data/postgres:/var/lib/postgresql/data

* Notice i added a new directory to the project ./data directory!

You can run the following in order for the volume to be attached:

docker-compose down

docker-compose up --build

Added by Igal Chernov

