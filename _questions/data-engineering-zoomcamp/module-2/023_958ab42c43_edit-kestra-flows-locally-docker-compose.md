---
id: 958ab42c43
question: How can I edit Kestra flows locally with Docker Compose and keep them version-controlled?
sort_order: 23
---

## How to edit Kestra flows locally with Docker Compose

By default, Kestra stores its flow definitions in a database. This means that every time you edit a flow through the web UI, the source of truth lives inside the container, not in your repository. That is fine for quick experiments, but for a real project you want flows version-controlled alongside the rest of the code and editable with your favourite IDE.

The solution is a **bind-mount** combined with Kestra's built-in **file watcher**. The idea goes like this: you mount a host directory into the container and tell Kestra to watch it. Any YAML file you create or modify in that folder is automatically synced into Kestra's catalog.

## 1. Bind-mount your flows directory

In `docker-compose.yml`, add a volume entry that maps a local folder (here `./flows`) to a path inside the container (here `/flows`):

```yaml
services:
  kestra:
    image: kestra/kestra:v1.3
    command: server standalone
    volumes:
      - kestra-data:/app/storage
      - /var/run/docker.sock:/var/run/docker.sock
      - /tmp/kestra-wd:/tmp/kestra-wd
      - ./flows:/flows
```

With this single line, anything you put in `./flows` on the host appears at `/flows` inside the container.

## 2. Enable the file watcher

Kestra uses Micronaut under the hood. You can activate its file-system watcher through the `KESTRA_CONFIGURATION` environment variable:

```yaml
services:
  kestra:
    environment:
      KESTRA_CONFIGURATION: |
        micronaut:
          io:
            watch:
              enabled: true
              paths:
                - /flows
```

The `paths` list must point to the **container-side** path — `/flows` in our case, not the host path.

## 3. Write your flows as local YAML files

Create any flow definition inside the `./flows` directory on your host. For example, `./flows/dev.hello.yml`:

```yaml
id: hello
namespace: dev
tasks:
- id: say_hi
  type: io.kestra.plugin.core.log.Log
  message: "Hello from a local file!"
```

As soon as you save the file, the watcher picks up the change and Kestra imports (or updates) the flow. You can verify it in the web UI at `http://localhost:8080`.

## How the sync works

- From **Host** to **Kestra** is automatic thanks to the watcher. Every time a YAML file is created or modified in the watched directory, Kestra upserts the corresponding flow.
- From **Kestra** to **Host** does *not* happen. If you edit a flow through the web UI, the change is written to the database only; the YAML file on the host is not updated. To keep things consistent, treat the local files as the single source of truth and avoid editing flows in the UI.

## Putting it all together

A minimal `docker-compose.yml` that includes everything discussed above:

```yaml
services:
  postgres:
    image: postgres:18
    environment:
      POSTGRES_DB: kestra
      POSTGRES_USER: kestra
      POSTGRES_PASSWORD: k3str4
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d kestra -U kestra"]
      interval: 30s
      timeout: 10s
      retries: 10

  kestra:
    image: kestra/kestra:v1.3
    command: server standalone
    user: "root"
    volumes:
      - kestra-data:/app/storage
      - /var/run/docker.sock:/var/run/docker.sock
      - /tmp/kestra-wd:/tmp/kestra-wd
      - ./flows:/flows
    environment:
      KESTRA_CONFIGURATION: |
        micronaut:
          io:
            watch:
              enabled: true
              paths:
                - /flows
        datasources:
          postgres:
            url: jdbc:postgresql://postgres:5432/kestra
            driverClassName: org.postgresql.Driver
            username: kestra
            password: k3str4
        kestra:
          repository:
            type: postgres
          queue:
            type: postgres
        tasks:
          tmp-dir:
            path: /tmp/kestra-wd/tmp
    ports:
      - "8080:8080"
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  kestra-data:
```

Run `docker compose up -d`, drop a YAML flow into `./flows`, and it will appear in Kestra within seconds, fully version-controlled and editable from your host machine.

For more information, check Kestra's official [guide to sync local flows](https://kestra.io/docs/how-to-guides/local-flow-sync).