---
id: ac52bea382
question: 'pgAdmin: persist server / connection settings across container restarts'
sort_order: 22
---

By default, the `dpage/pgadmin4` image stores its config (registered servers, query history, etc.) inside the container — so it's lost every time you `docker compose down`.

To persist it, mount `/var/lib/pgadmin` to a Docker volume. Use a named volume rather than a host-bind, because pgAdmin runs as user 5050 and host permissions tend to fight you:

```yaml
services:
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    volumes:
      - "pgadmin-data:/var/lib/pgadmin"
    ports:
      - "8080:80"

volumes:
  pgadmin-data:
```

After this, your pgAdmin servers and dashboards survive `docker compose down` and `docker compose up`.

## If you really want a host-bind mount

You'll need to fix permissions before mounting. pgAdmin's container user is 5050:

```bash
mkdir -p ./pgadmin_data
sudo chown -R 5050:5050 ./pgadmin_data
```

Then:

```yaml
volumes:
  - "./pgadmin_data:/var/lib/pgadmin"
```

If you skip the chown step, pgAdmin will fail to start with a permission error.

## On GCP / cloud VMs

Same approach works — use a named volume rather than host-bind to avoid filesystem permission quirks on the cloud disk.
