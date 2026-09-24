---
id: 4a31d1d4f2
question: Why does my GitHub Actions workflow that uses a Postgres service work on
  GitHub Actions but fail under `act` with `localhost` connection refused, and what
  hostname should I use?
sort_order: 4
---

When running a workflow with `act`, your “service” container (e.g., `postgres:16`) is on a separate Docker network from the job container, and its port is not published to the job container’s loopback. On GitHub Actions, service ports are effectively reachable from `localhost` on the runner, so `localhost:5432` works there.

Under `act`, connect using the service hostname defined under `services` (the key name), not `localhost`. For a workflow like:

- `services: postgres: ...`

use `postgres:5432` as the host.

A reliable fix that works in both environments is to parameterize the host with a fallback:

- In the job, set `RELAY_DATABASE_URL` to use `${{ vars.DB_HOST || 'localhost' }}`.
- When running locally with `act`, pass `--var DB_HOST=postgres` so the connection string points to the service container.

Sanity checks:
- In the `act` network, both containers should appear in `docker network inspect <act-…-test-network>`.
- Inside the job container, `getent hosts postgres` should resolve.
- If the Postgres service logs show it’s healthy in `act` but the job gets `connection refused` to loopback addresses (`127.0.0.1`/`::1`), it’s almost always this networking difference—not the healthcheck.