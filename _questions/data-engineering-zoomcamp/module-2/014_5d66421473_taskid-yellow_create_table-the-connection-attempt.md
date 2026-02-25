---
id: 5d66421473
question: 'taskid: yellow_create_table The connection attempt failed. Host.docker.internal'
sort_order: 14
---

If you're using Linux, you might encounter "Connection Refused" errors when connecting to the Postgres DB from within Kestra. This is because `host.docker.internal` works differently on Linux.

To address this issue:

- Use the modified Docker Compose file mentioned in the "02-workflow-orchestration" README troubleshooting tips.
- Run both Kestra and its dedicated Postgres DB, along with the Postgres DB for exercises, all together using Docker Compose.
- Access the Postgres DB within Kestra by using the container name `postgres_zoomcamp` instead of `host.docker.internal` in `pluginDefaults`.

Make sure to modify the `pluginDefaults` in the following files:

- `2_postgres_taxi_scheduled.yaml`
- `02_postgres_taxi.yaml`

Example `pluginDefaults` configuration:

```yaml
pluginDefaults:
  - type: io.kestra.plugin.jdbc.postgresql
    values:
      url: jdbc:postgresql://postgres_zoomcamp:5432/postgres-zoomcamp
      username: kestra
      password: k3str4
```
