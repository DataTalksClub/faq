---
id: 30622af850
question: How do I ensure that the ingestion pipeline runs successfully and in what
  order should I build and run the containers?
sort_order: 2
---

### Step 1: Create a common network

Ensure that you have created a common network (`pg-network`). This allows several containers to communicate with each other. On top of this network you will run:

1. Postgres container
2. The Dockerized ingestion script container
3. pgAdmin container

```bash
docker network create pg-network
```

### Step 2: Run the Postgres container

Once you’ve created the network, start running each container one by one. First, run the Postgres container:

```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ny_taxi_postgres_data:/var/lib/postgresql \
    -p 5432:5432 \
    --network=pg-network \
    --name pgdatabase \
    postgres:16
```

If `postgres:18` causes issues, use `postgres:16` as shown above.

### Step 3: Build the Docker container for the pipeline

Ensure your current working directory is `/pipeline`, then build:

```bash
docker build -t taxi_ingest:v001 .
```

### Step 4: Run the ingestion container

```bash
docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --pg_user=root \
    --pg_pass=root \
    --pg_host=pgdatabase \
    --pg_port=5432 \
    --pg_db=ny_taxi \
    --year=2021 \
    --month=1 \
    --target_table=yellow_taxi_trips
```

Make sure that you use the parameters in the command exactly as defined in your script. For example, if your script uses `--pg_user` then use `--pg_user`; if it uses `--user` then change the command accordingly.

### Step 5 (Optional): Validate the ingested records

To check if your records reached the Postgres table, run pgcli:

```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

List tables:

```sql
\dt
```

Check row count:

```sql
SELECT COUNT(*) FROM yellow_taxi_trips;
```
