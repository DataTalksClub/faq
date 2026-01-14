---
id: 30dcc71db8
question: How can I back up and restore PostgreSQL data stored in a Docker volume?
sort_order: 25
---

- Method 1: Docker volume backup
  ```bash
  # List Docker volumes
  docker volume ls
  # Backup while the container is running
  docker run --rm \
  -v ny_taxi_postgres_data:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/postgres_backup.tar.gz /data
  # Restore
  docker run --rm \
  -v ny_taxi_postgres_data:/data \
  -v $(pwd):/backup \
  ubuntu tar xzf /backup/postgres_backup.tar.gz -C /
  ```
- Method 2: Using pg_dump
  ```bash
  # Backup
  docker exec -t postgres_container pg_dump -U root -d ny_taxi > ny_taxi_backup.sql
  # Restore
  docker exec -i postgres_container psql -U root -d ny_taxi < ny_taxi_backup.sql
  ```
- Method 3: Copying the host directory
  ```bash
  # When using a host-mounted directory in docker-compose.yaml
  cp -r ./ny_taxi_postgres_data ./ny_taxi_postgres_data_backup
  ```