---
id: e43abaa421
question: 'docker compose: installation problems (binary not found, exec format error,
  credentials error, dial unix /var/run/docker.sock)'
sort_order: 24
---

Most "docker-compose" installation problems on Linux/WSL fall into a small handful of categories.

## "docker-compose: command not found" / "still not available"

The downloaded file from the docker/compose releases page has a long platform-suffixed name like `docker-compose-linux-x86_64`. Rename it and put it on your `PATH`:

```bash
sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Modern Docker (20.10+) ships compose v2 as `docker compose` (with a space). If you have a recent Docker install, you may not need a separate `docker-compose` binary at all — just use `docker compose up`.

## Picking the right binary for your platform

Use `uname` to determine which file to download:

```bash
uname -s   # operating system, usually 'Linux'
uname -m   # architecture, e.g. 'x86_64' or 'aarch64'
```

Then download the matching release, e.g.:

```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Pin a specific release if you need reproducibility (substitute `latest/download` with `download/<version>`).

## "cannot execute binary file: Exec format error"

The architecture doesn't match. ARM64 machines (Apple Silicon, ARM Linux, some VMs) need the `aarch64` binary, not `x86_64`. Re-download with `uname -m` substituted correctly.

## "error getting credentials" / "docker-credential-desktop not found"

Docker is looking for a credential helper that isn't installed. Two fixes:

```bash
# Quick: install pass (resolves it on most Linux distros)
sudo apt install pass
```

Or edit `~/.docker/config.json` and rename `credsStore` to `credStore` (the helper-less default), or remove the line entirely.

## "dial unix /var/run/docker.sock: connect: permission denied"

Your user isn't in the `docker` group. Add it:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
# log out and back in for the group change to apply
```
