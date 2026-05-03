---
id: b9cd2aaccb
question: 'pgcli / Postgres: troubleshooting connection failures (FATAL: password
  auth, role does not exist, database does not exist, connection refused, port in
  use)'
sort_order: 1
---

The various Postgres connection errors students hit in week 1 almost always trace back to one of three problems. Before changing anything, identify which:

```
connection failed: connection to server at "localhost" port 5432 failed: Connection refused
FATAL: password authentication failed for user "root"
FATAL: role "root" does not exist
FATAL: database "ny_taxi" does not exist
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed
```

## Step 1: confirm the right Postgres is reachable

Run:

```bash
docker ps
```

You should see the `postgres:13` (or `postgres:16`/`postgres:18`) container with port mapping `0.0.0.0:5432->5432/tcp`. If not, start it:

```bash
docker compose up -d
# or, for the standalone docker run:
docker run -it -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=ny_taxi \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 postgres:16
```

## Step 2: check whether port 5432 is already taken on your host

A locally installed Postgres ("Postgres.app", `apt install postgresql`, the Windows installer, the Mac Homebrew formula) often listens on 5432. When you map the Docker container to the same port, the connection silently goes to the wrong instance — which is usually the source of "FATAL: password authentication failed for user root" or "role root does not exist" (the local install doesn't know about the `root` user).

Linux/Mac:

```bash
sudo lsof -i :5432
```

Windows: open Services (`services.msc`) and look for any `postgresql-x64-XX` service.

You have two options:

- Stop the local Postgres:
  - Linux: `sudo service postgresql stop`
  - Mac (Homebrew): `launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist`
  - Windows: stop the `postgresql-x64-XX` service in Services.

- Or change the Docker mapping to a different host port and connect to that port:

  ```bash
  -p 5433:5432
  # then
  pgcli -h localhost -p 5433 -u root -d ny_taxi
  ```

## Step 3: match host names between the script and the runtime

If the connection error mentions a host name like `pgdatabase` or `pg-database` and says "could not translate host name", you are running an ingestion script that points at a Docker service name from outside the Docker network. Pick one:

- Run the script from inside the same Docker network and use the service name (`pgdatabase`).
- Run the script from your host machine and use `localhost` (or `127.0.0.1`).

For the Dockerized ingestion job the course shows, both the container and the Postgres container must share a Docker network — `--network=pg-network` on `docker run`, or the implicit network in `docker compose`.

## Step 4: persistent data corruption / "database ny_taxi does not exist"

If the database existed before but the `FATAL: database ny_taxi does not exist` error appears now, your Postgres container probably started with an empty data directory. Two common reasons:

- The volume mount path is wrong, so a new empty data dir is being initialised every time.
- Volumes were pruned (e.g. `docker compose down -v`).

Either restore data from backup, or wipe the volume and re-ingest:

```bash
docker compose down -v
docker compose up -d
# then re-run the ingestion script
```

## Step 5: client-side issues (pgcli specifically)

If pgcli prints `ImportError: no pq wrapper available`, it can't find `libpq` — install the binary psycopg:

```bash
uv add "psycopg[binary]"
# or
pip install "psycopg[binary]"
```

If pgcli appears to hang at the password prompt on Windows Git Bash, prefix it with `winpty`:

```bash
winpty pgcli -h localhost -p 5432 -u root -d ny_taxi
```

Or use Windows Terminal / VS Code's integrated terminal instead of Git Bash.

## Quick reference

- `Connection refused` → Postgres isn't running, or it's on a different port. Check `docker ps`.
- `FATAL: password authentication failed for user "root"` → almost always a port collision with a locally-installed Postgres.
- `FATAL: role "root" does not exist` → same as above (local install doesn't have a `root` user).
- `FATAL: database "ny_taxi" does not exist` → Postgres init didn't run, or the volume is empty.
- `could not translate host name "pgdatabase"` → wrong host name for where you're connecting from (host vs container network).
