---
id: 6c63eb7b83
question: Why does my ingestion script fail when using localhost as the Postgres host
  in Docker?
sort_order: 114
---

Inside a Docker container, localhost refers to the container itself, not the Postgres container. If you try to connect to Postgres using localhost from your ingestion script, the connection will fail because the Postgres container is a separate container on the same Docker network. Fixes:
- In your connection settings, point to the Postgres service by its Docker Compose service name (for example, `postgres`) instead of `localhost`.
- Use the correct port (default 5432) and the proper credentials.

Example connection strings (adjust to your library):
- For URL-style: `postgresql://USER:PASSWORD@postgres:5432/DATABASE`
- For host/port: host=`postgres`, port=`5432`, user=`USER`, password=`PASSWORD`, dbname=`DATABASE`.

If your Compose file uses a different service name, use that instead. Ensure both containers share the same Docker network and that the Postgres service is up.