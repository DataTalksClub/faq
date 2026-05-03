---
id: 30dcc71db8
question: How can I back up and restore PostgreSQL data stored in a Docker volume?
sort_order: 11
---

### Method 1: Docker volume backup

List Docker volumes:

```bash
docker volume ls
```

Backup while the container is running:

```bash
docker run --rm \
    -v ny_taxi_postgres_data:/data \
    -v $(pwd):/backup \
    ubuntu tar czf /backup/postgres_backup.tar.gz /data
```

Restore:

```bash
docker run --rm \
    -v ny_taxi_postgres_data:/data \
    -v $(pwd):/backup \
    ubuntu tar xzf /backup/postgres_backup.tar.gz -C /
```

### Method 2: Using `pg_dump`

Backup:

```bash
docker exec -t postgres_container pg_dump -U root -d ny_taxi > ny_taxi_backup.sql
```

Restore:

```bash
docker exec -i postgres_container psql -U root -d ny_taxi < ny_taxi_backup.sql
```

### Method 3: Copying the host directory

When using a host-mounted directory in `docker-compose.yaml`:

```bash
cp -r ./ny_taxi_postgres_data ./ny_taxi_postgres_data_backup
```