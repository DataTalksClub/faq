---
id: 1700cb2bd4
question: 'docker compose: "could not translate host name pgdatabase / pg-database
  to address" — hostname does not resolve'
sort_order: 15
---

This error means your container is looking for another service by name on a Docker network, but they aren't on the same network. Common variants:

```
sqlalchemy.exc.OperationalError: could not translate host name "pgdatabase" to address: Name or service not known
Unable to connect to server: could not translate host name 'pg-database' to address: Name does not resolve
network <hash> not found
```

## What's happening

Docker network DNS only resolves service names within the same network. Two reasons it might fail:

1. The ingestion container was started with `--network <name>` but `<name>` doesn't match the network compose actually created. By default, `docker compose` creates a network named after the project directory plus `_default` (e.g. `2docker_default`).

2. Your ingestion script is hardcoded to use a host name like `pgdatabase`, but the compose service is actually called `pgdatabase-1`, or you're running the script outside Docker entirely.

## Fix

1. List networks and confirm the actual name compose created:

   ```bash
   docker network ls
   ```

   Pass that exact name when running the ingestion container:

   ```bash
   docker run --network=<actual_network_name> taxi_ingest:v001 ...
   ```

   Or pin the network name in your `docker-compose.yml` so it doesn't depend on the directory name:

   ```yaml
   networks:
     pg-network:
       name: pg-network
   ```

2. Make the host name in your script match the compose service name. If your service is called `pgdatabase`, the script should use `--pg_host=pgdatabase` (when running inside Docker) or `--pg_host=localhost` (when running on the host).

3. Avoid hostnames with dashes when possible — `pgdatabase` is more reliable than `pg-database` across some networks/DNS configs.

4. If `docker network ls` shows a stale network from a previous run, prune it: `docker network prune` (after stopping the relevant containers).

## Working compose snippet

```yaml
services:
  pgdatabase:
    image: postgres:16
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: ny_taxi
    volumes:
      - "pg-data:/var/lib/postgresql/data"
    ports:
      - "5432:5432"
    networks:
      - pg-network

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - "8080:80"
    networks:
      - pg-network

networks:
  pg-network:
    name: pg-network

volumes:
  pg-data:
```
