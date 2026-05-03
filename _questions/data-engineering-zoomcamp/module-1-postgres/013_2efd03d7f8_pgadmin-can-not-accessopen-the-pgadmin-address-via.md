---
id: 2efd03d7f8
question: pgAdmin - Can not access/open the PgAdmin address via browser
sort_order: 13
---

I am using a Mac Pro device and connect to the GCP Compute Engine via Remote SSH - VSCode. But when trying to run the PgAdmin container via `docker run` or `docker compose`, I couldn't access the PgAdmin address via my browser. After modifications, I was able to access it.

### Solution #1:

Modify the `docker run` command:

```bash
docker run --rm -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="pgadmin" \
  -e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \
  -e PGADMIN_LISTEN_ADDRESS=0.0.0.0 \
  -e PGADMIN_LISTEN_PORT=5050 \
  -p 5050:5050 \
  --network=de-zoomcamp-network \
  --name pgadmin-container \
  --link postgres-container \
  -t dpage/pgadmin4
```

### Solution #2:

Modify the `docker-compose.yaml` configuration and use the `docker compose up` command:

```yaml
pgadmin:
  image: dpage/pgadmin4
  container_name: pgadmin-container
  environment:
    - PGADMIN_DEFAULT_EMAIL=admin@admin.com
    - PGADMIN_DEFAULT_PASSWORD=pgadmin
    - PGADMIN_CONFIG_WTF_CSRF_ENABLED=False
    - PGADMIN_LISTEN_ADDRESS=0.0.0.0
    - PGADMIN_LISTEN_PORT=5050
  volumes:
    - "./pgadmin_data:/var/lib/pgadmin/data"
  ports:
    - "5050:5050"
  networks:
    - de-zoomcamp-network
  depends_on:
    - postgres-container
```