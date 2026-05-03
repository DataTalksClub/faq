---
id: a950fda271
question: 'Docker-Compose: PgAdmin – no database in PgAdmin'
sort_order: 21
---

When you log into PgAdmin and see an empty database, the following solution can help:

Run:
   
```bash
docker-compose up
```

And at the same time run:

```bash
docker build -t taxi_ingest:v001 .

# NETWORK NAME IS THE SAME AS THAT CREATED BY DOCKER COMPOSE
docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
  --user=postgres \
  --password=postgres \
  --host=db \
  --port=5432 \
  --db=ny_taxi \
  --table_name=green_tripdata \
  --url=${URL}
```

It's important to use the same `--network` as stated in the `docker-compose.yaml` file.

The `docker-compose.yaml` file might not specify a network, as shown below:

```yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      ...
    ports:
      - '5433:5432'
    volumes:
      - ...
  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      ...
    ports:
      - '8080:80'
    volumes:
      - ...

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

If the network name is not specified, it is generated automatically: The name of the directory containing the `docker-compose.yaml` file in lowercase + `_default`.

You can find the network’s name when running `docker-compose up`:

```
pg-database Pulling pg-database Pulled 
Network week_1_default  Creating
Network week_1_default  Created
```