---
id: 30622af850
question: How do I ensure that the ingestion pipeline runs successfully and in what
  order should I build and run the containers?
sort_order: 60
---

Step 1: Create a common network
Ensure that you have created a common network (`pg-network`). This is to ensure that you run several containers in the same network so that they can communicate with each other.
Pg-network is the broader network layer on top of which you will run -
1. Postgres container,
2. the Dockerized script container (the container which you will have your ingestion script)
3. pgadmin container
Command:
```bash
docker network create pg-network
```

Step 2: Run the Postgres container
Once you’ve created the network, start running each container one-by-one.  First, run the Postgres container
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
Remember, if `postgres:18` causes issues, use `postgres:16` as mentioned above

Step 3: Build the docker container for the pipeline
Ensure your current working directory is /pipeline. Then, run this command to build your container -
```bash
docker build -t taxi_ingest:v001 .
```

Step 4: Run the ingestion container
Ensure your current working directory is /pipeline. Then, run this command to build your container -
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
Make sure that you use the parameters in the command exactly same as what you have in your script. For example, if your script as the click parameter `–pg_user` then use `pg_user`, else if it is something like `--user` then change the above command to include `--user` instead of `--pg_user`

Step 5 (Optional): To validate if your records reached the table
To validate if your records really reached the Postgres table, run PGCLI using the following command -
```bash
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```
Once inside pgcli, run the following to get table names -
```postgres
\dt
```
Then, to validate how many rows have been ingested, run the following -
```postgres
SELECT COUNT(*) FROM yellow_taxi_trips
```
