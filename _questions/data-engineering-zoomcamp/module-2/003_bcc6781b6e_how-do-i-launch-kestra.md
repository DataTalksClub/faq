---
id: bcc6781b6e
question: How do I launch Kestra?
sort_order: 3
---

To launch Kestra, follow these instructions:

**For Linux**

Start Docker with the following command:

```bash
docker run \
  --pull=always \
  --rm \
  -it \
  -p 8080:8080 \
  --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp \
  kestra/kestra:latest server local
```

Once it is running, you can log in to the dashboard at `localhost:8080`.

**For Windows**

Refer to the Kestra GitHub repository for detailed instructions: [https://github.com/kestra-io/kestra](https://github.com/kestra-io/kestra)

Sample `docker-compose` for Kestra:

```yaml
kestra:
  build: .
  image: kestra/kestra:latest
  container_name: kestra
  user: "0:0"
  environment:
    DOCKER_HOST: tcp://host.docker.internal:2375  # for Windows
    KESTRA_CONFIGURATION: |
      kestra:
        repository:
          type: h2
        queue:
          type: memory
        storage:
          type: local
          local:
            basePath: /app/storage
        tasks:
          tmp-dir:
            path: /app/tmp
        plugins:
          repositories:
            - id: central
              type: maven
              url: [repo.maven.apache.org](https://repo.maven.apache.org/maven2)
          definitions:
            - io.kestra.plugin.core:core:latest
            - io.kestra.plugin.scripts:python:1.3.4
            - io.kestra.plugin.http:http:latest
    KESTRA_TASKS_TMP_DIR_PATH: /app/tmp
  ports:
    - "8080:8080"
  volumes:
    - //var/run/docker.sock:/var/run/docker.sock  # Windows path
    - /yourpath/.dbt:/app/.dbt
    - /yourpath/kestra/plugins:/app/plugins
    - /yourpath/kestra/workflows:/app/workflows
    - /yourpath/kestra/storage:/app/storage
    - /yourpath//kestra/tmp:/app/tmp
    - /yourpath//dbt_prj:/app/workflows/dbt_project
    - /yourpath//my-creds.json:/app/.dbt/my-creds.json
  command: server standalone
```