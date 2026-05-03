---
id: 05e6bff42c
question: "pgcli: PermissionError: [Errno 13] Permission denied: '~/.config/pgcli'"
sort_order: 4
---

```
PermissionError: [Errno 13] Permission denied: '/Users/<you>/.config/pgcli'
```

This means pgcli can't write its config dir. Two common causes.

## Cause 1: someone ran pgcli with sudo earlier

Running `sudo pgcli ...` once creates `~/.config/pgcli` owned by root. Subsequent runs as your normal user can't write there. Fix the ownership:

```bash
sudo chown -R "$USER" ~/.config/pgcli
```

Going forward, install and run pgcli without `sudo` — install it into a project venv (recommended) or `pip install --user pgcli` so you don't need root.

## Cause 2: pgcli installed into a system Python you can't write to

Install pgcli into an isolated environment instead. Recommended path is `uv`:

```bash
uv add pgcli "psycopg[binary]"
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

Or with a plain `venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pgcli "psycopg[binary]"
```

Either way, run pgcli from inside the activated environment (or via `uv run pgcli`) — never with `sudo`.
