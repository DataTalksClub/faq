---
id: 6901ee30ae
question: Why doesn’t Docker Compose automatically load all my environment files (e.g.,
  `.env` and `.env.compose`), and how can I ensure the correct variables reach the
  containers?
sort_order: 6
---

Docker Compose treats environment variables in two different roles: (1) variables used to substitute values inside the Compose configuration itself, and (2) environment variables that exist inside the running containers. Those aren’t automatically the same.

1) `.env` is for Compose file substitution, not “everything”
- By default, Compose will read a `.env` file for variable interpolation when building your `docker-compose.yaml`.
- Compose does not automatically load additional env files you create (like `.env.compose`) unless you tell it to.

2) Explicitly pass multiple env files when you run Compose
Example:
- `.env` contains `API_KEY=...`
- `.env.compose` contains `POSTGRES_PASSWORD=...`

Run:
```bash
docker compose --env-file .env --env-file .env.compose up --build
```
If the same variable is defined in multiple files, later `--env-file` arguments override earlier ones.

3) Ensure variables actually reach the container
Passing `--env-file` makes variables available to Compose for interpolation, but it does not magically inject every variable into every service.

Common patterns:
- Map variables into `environment:` explicitly:
  - In your service, set `environment:` values like `${API_KEY}` and `${POSTGRES_PASSWORD}`.
- Or use `env_file:` on the service to load env vars directly into that container:
  - List both `.env` and `.env.compose` under `env_file`.

4) Debug the resolved configuration
Use Compose `config` to see what Compose will generate:
```bash
docker compose --env-file .env --env-file .env.compose config
```
Be careful: the output may include secrets, so don’t share it publicly.

(References: Docker docs on variable interpolation and setting environment variables in containers.)