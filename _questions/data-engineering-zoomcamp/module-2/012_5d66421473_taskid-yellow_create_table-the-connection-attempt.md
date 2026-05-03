---
id: 5d66421473
question: 'Kestra: "host.docker.internal" connection failures on Linux'
sort_order: 12
---

`host.docker.internal` is a Docker Desktop convenience that resolves to the host machine. On native Linux Docker (and many Linux server setups) it doesn't resolve by default, so Kestra tasks that try to reach Postgres or other services via `host.docker.internal` fail with errors like:

```
The connection attempt failed.
could not translate host name "host.docker.internal" to address: Name or service not known
```

You have two options.

## Option 1 (recommended): use the container service name

If Kestra and Postgres are in the same `docker-compose.yml`, just refer to Postgres by its service name. Replace `host.docker.internal` with the service name (e.g. `postgres_zoomcamp`) in `pluginDefaults`:

```yaml
pluginDefaults:
  - type: io.kestra.plugin.jdbc.postgresql
    values:
      url: jdbc:postgresql://postgres_zoomcamp:5432/postgres-zoomcamp
      username: kestra
      password: k3str4
```

Apply this in flows like `02_postgres_taxi.yaml` and `2_postgres_taxi_scheduled.yaml`.

## Option 2: add `extra_hosts` so `host.docker.internal` resolves on Linux

Add an `extra_hosts` entry to the Kestra service in `docker-compose.yml`:

```yaml
services:
  kestra:
    image: kestra/kestra:latest
    extra_hosts:
      - "host.docker.internal:host-gateway"
    # ...
```

For the `dbt-build` task (or any other task using `taskRunner` with Docker), add `extraHosts` there too:

```yaml
taskRunner:
  type: io.kestra.plugin.scripts.runner.docker.Docker
  extraHosts:
    - "host.docker.internal:host-gateway"
```

Option 1 is cleaner for inter-container communication; Option 2 is needed only when Kestra genuinely needs to reach a service running on the host (not in a sibling container).
