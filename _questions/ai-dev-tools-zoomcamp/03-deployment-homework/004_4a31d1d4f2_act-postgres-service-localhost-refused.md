---
id: 4a31d1d4f2
question: Why is the Postgres service healthy under `act` while my job gets "connection
  refused" on `localhost`, and what hostname should I use?
sort_order: 4
---

For HW3 you only run the workflow with act, so using `postgres` as the host is enough.

Under `act`, the job itself runs in a container, and the service container (e.g., `postgres:16`) is a separate container on the same Docker network. Its port isn't on the job container's loopback, so `localhost:5432` is refused. Connect using the service name defined under `services` (the key name) instead: for `services: postgres: ...`, use `postgres:5432`.

On a GitHub-hosted runner the job runs directly on the VM, so `localhost:5432` works there, but only if the service maps the port (`ports: ["5432:5432"]`).

If you want the same workflow to work in both places, parameterize the host with a fallback:

```yaml
services:
  postgres:
    image: postgres:16
    ports: ["5432:5432"]      # needed for localhost on GitHub-hosted runners
steps:
  - env:
      RELAY_DATABASE_URL: postgresql+psycopg://relay:relay@${{ vars.DB_HOST || 'localhost' }}:5432/relay
```

Run locally with `act --var DB_HOST=postgres`.

Sanity checks:
- In the `act` network, both containers should appear in `docker network inspect <act-…-network>`.
- Inside the job container, `getent hosts postgres` should resolve.
- If the Postgres service logs show it's healthy in `act` but the job gets `connection refused` to loopback addresses (`127.0.0.1`/`::1`), it's almost always this networking difference, not the healthcheck.
