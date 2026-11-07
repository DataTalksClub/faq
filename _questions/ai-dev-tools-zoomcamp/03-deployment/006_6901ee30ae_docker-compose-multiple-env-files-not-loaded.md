---
id: 6901ee30ae
question: 'Why doesn’t Docker Compose automatically load all my environment files (e.g., `.env` and `.env.compose`), and how can I ensure the correct variables reach the containers?'
sort_order: 6
---

Docker Compose uses environment files in two different ways: to substitute values in the Compose file and to set environment variables inside a container. These are separate steps.

Compose uses `.env` for variable interpolation by default.

To use more than one file for interpolation, pass each with `--env-file`:

```bash
docker compose --env-file .env --env-file .env.compose up --build
```

When the files define the same variable, the later file takes precedence. To pass a value into a container, either map it under the service's `environment` setting or list the files under that service's `env_file` setting. The CLI's `--env-file` option doesn't automatically inject every variable into every container.

Check the resolved Compose configuration with:

```bash
docker compose --env-file .env --env-file .env.compose config
```

The output can contain secrets, so don't share it publicly. See Docker's documentation for [variable interpolation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/) and [setting environment variables in containers](https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/).
