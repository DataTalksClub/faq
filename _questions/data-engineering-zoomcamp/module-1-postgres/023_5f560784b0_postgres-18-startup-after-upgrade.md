---
id: 5f560784b0
question: Postgres fails to start after upgrading from postgres:16 to postgres:18
  in Docker
sort_order: 23
---

Postgres 18 changes how the data directory is structured inside Docker containers. While Postgres ≤16 stored data under /var/lib/postgresql/data, Postgres 18 expects the volume to be mounted at /var/lib/postgresql. If an existing volume created with an older Postgres version is reused without updating the mount path, Postgres 18 will detect an incompatible layout and exit during startup. This can appear as DNS resolution errors or failed connections from pgAdmin or ingestion jobs. For Week 1 setups, the fix is to update the volume mount path, remove the old volume, and recreate the containers so Postgres 18 can initialize a new data directory.

## Proposed Fix (Week 1 setups)
- Update the volume mount path to /var/lib/postgresql (instead of /var/lib/postgresql/data).
- Remove the old volume that was created with Postgres 16.
- Recreate the containers so Postgres 18 initializes a fresh data directory.

### Example commands
- Running with docker run (adjust as needed):
```
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="admin" \
  -e POSTGRES_DB="ny_taxi" \
  -v "/path/to/ny_taxi_postgres_data":"/var/lib/postgresql" \
  -p 5432:5432 \
  postgres:18
```

- For docker-compose, mount the volume to /var/lib/postgresql:
```
volumes:
  ny_taxi_postgres_data:

services:
  postgres:
    image: postgres:18
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: ny_taxi
    volumes:
      - ny_taxi_postgres_data:/var/lib/postgresql
```

- Remove the old volume (list and remove):
```
docker volume ls
docker volume rm <old-volume-name>
```

- Recreate containers:
```
docker-compose down
docker-compose up -d
```

### Notes
- Ensure you have a backup of any important data before removing volumes.
- After restarting, verify that Postgres starts and the data directory is initialized under /var/lib/postgresql.
