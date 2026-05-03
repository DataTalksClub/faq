---
id: 87e92edf02
question: 'docker on Windows: volume mount path syntax (Git Bash, MINGW, paths with
  spaces, "ny_taxi_postgres_data is empty")'
sort_order: 9
---

Mounting host paths on Windows is the single biggest source of week 1 confusion. Symptoms:

- `ny_taxi_postgres_data` appears empty even though Postgres started.
- `Docker: invalid reference format: repository name must be lowercase`
- `Error response from daemon: invalid mode: \Program Files\Git\var\lib\postgresql\data`
- A folder with a weird name like `ny_taxi_postgres_data;C` is created.

## Root cause

Git Bash / MINGW64 mangles Unix-style paths into Windows-style paths before passing them to Docker, and the rules differ depending on quoting, leading slashes, and whether your path contains spaces. The cleanest workaround on Windows is to skip the host-bind mount entirely (see [the named-volume FAQ](#0beb2b5df7)) — but if you need the bind mount, here's what tends to work.

## Use a path without spaces

Move your project out of any directory with spaces (e.g. from `C:\Users\Alexey Grigorev\git\...` to `C:\git\...`). Many of the path-syntax issues simply go away once the path is clean.

## Try these `-v` syntax variants in order

```bash
# 1. Forward slashes, with leading slash on the drive letter:
-v "/c/Users/me/project/ny_taxi_postgres_data:/var/lib/postgresql/data"

# 2. Double leading slashes (some MINGW versions need this):
-v "//c/Users/me/project/ny_taxi_postgres_data:/var/lib/postgresql/data"

# 3. With a colon after the drive letter:
-v "/c:/Users/me/project/ny_taxi_postgres_data:/var/lib/postgresql/data"

# 4. Backslashes in quotes:
-v "c:\Users\me\project\ny_taxi_postgres_data:/var/lib/postgresql/data"

# 5. Use $(pwd) — wrap in quotes:
-v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data"
```

## Also try `winpty`

If the command appears to do nothing or hangs:

```bash
winpty docker run -it ...
```

## If `Docker: invalid reference format: repository name must be lowercase`

This usually means the shell didn't substitute `$(pwd)` properly and inserted a literal `\Program Files\Git\...` into the path. Use one of the explicit paths above instead of `$(pwd)`.

## If you see a folder called `ny_taxi_postgres_data;C` get created

The volume mount string was misparsed. Delete the bogus folder and retry with `//c/...` (double leading slash) instead of `/c/...`.

## On Mac, just wrap `$(pwd)` in quotes

```bash
docker run -it \
  -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=ny_taxi \
  -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
  -p 5432:5432 \
  postgres:16
```

## Last resort: use a named volume

If none of the bind-mount syntaxes work, switch to a named volume. The data still persists, you just don't see it in your project folder:

```bash
-v ny_taxi_postgres_data:/var/lib/postgresql/data
```

This is the recommended approach on Windows.
