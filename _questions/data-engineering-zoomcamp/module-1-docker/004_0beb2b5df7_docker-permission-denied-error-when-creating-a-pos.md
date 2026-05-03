---
id: 0beb2b5df7
question: 'docker + Postgres: permission errors on the data directory (chown / could
  not change permissions / could not create / build context errors)'
sort_order: 4
---

When you start the Postgres container with a host-bind mount (`-v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data`), the Postgres process inside the container runs as the `postgres` user (UID 999) and tries to chown the data dir. If the host filesystem doesn't permit that — common on macOS, Windows file systems mounted into WSL, certain Linux configurations, and when your build context picks up the same dir — you'll see one of:

```
initdb: error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
chown /path/to/ny_taxi_postgres_data: permission denied
docker: Error response from daemon: error while creating mount source path
docker build error checking context: can't stat '/path/to/ny_taxi_postgres_data'
failed to read dockerfile: error from sender: open ny_taxi_postgres_data: permission denied
```

You may also be unable to delete the host folder later because it's owned by UID 999.

## Recommended fix: use a named Docker volume instead of a host-bind mount

Named volumes are managed by Docker and don't have the cross-OS permission problems:

```bash
docker volume create --name dtc_postgres_volume_local
docker run -it \
  -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=ny_taxi \
  -v dtc_postgres_volume_local:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16
```

In `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: ny_taxi
    volumes:
      - "pg-data:/var/lib/postgresql/data"
    ports:
      - "5432:5432"

volumes:
  pg-data:
```

The volume's data lives inside Docker's storage area (find it with `docker volume inspect pg-data`).

## If you must use a host-bind mount (Linux)

Grant the container access to the directory:

```bash
sudo chown -R 999:999 ny_taxi_postgres_data/
# or
sudo chmod -R 755 ny_taxi_postgres_data/
```

Use `777` only as a last resort and only on local dev paths — it makes the dir world-writable.

To delete a folder that Docker created (now owned by UID 999):

```bash
sudo rm -rf ny_taxi_postgres_data/
```

## On macOS specifically

If you see the chown error and you're using Rancher Desktop or another Docker alternative, switch to Docker Desktop. Some non-Docker-Desktop runtimes don't handle the chown into bind mounts.

## "directory ... exists but is not empty"

```
initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
```

This means the volume already has Postgres data from a previous run with different superuser/password settings. Either:

- Clear the volume and let Postgres re-initialise it: `docker volume rm dtc_postgres_volume_local` (or `docker compose down -v` for a compose volume).
- Or use the same `POSTGRES_USER` / `POSTGRES_PASSWORD` you used the first time the data was initialised. The `POSTGRES_*` env vars only take effect on first init — after that they're ignored.

## "build error checking context"

If `docker build` fails with `can't stat '.../ny_taxi_postgres_data'` or "permission denied" on the data folder, the build context (the directory you ran `docker build` from) includes the data dir, and the build can't read it.

Either move the data folder out of the build context, or add it to `.dockerignore`:

```
ny_taxi_postgres_data/
```

Even better, use a named volume (above) so the data never lives in your project directory in the first place.
