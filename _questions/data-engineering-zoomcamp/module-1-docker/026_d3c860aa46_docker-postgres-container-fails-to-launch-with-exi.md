---
id: d3c860aa46
question: 'Docker: Postgres container fails to launch with exit code (1) when attempting
  to compose'
sort_order: 26
---

This issue arises because the Postgres database is not initialized before executing `docker-compose up -d`. While there are other potential solutions [discussed in this thread](https://forums.docker.com/t/one-of-the-postgres-containers-stops-as-soon-as-it-starts/74714/3), you can resolve it by initializing the database first. Then, the Docker Compose will work as expected.

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name=pg_database \
  postgres:13
```