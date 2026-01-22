---
id: 7f7aa5f5e6
question: 'PGCLI - ImportError: no pq wrapper available (including uv package manager
  fixes)'
sort_order: 71
---

This error occurs because psycopg cannot find the PostgreSQL client library (libpq). The simplest solution with uv is to install the binary version of psycopg, which bundles the required library.

Solution 1: Add psycopg-binary (Recommended)
```
uv add psycopg-binary

uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

Solution 2: Manually edit pyproject.toml
```
[project]
dependencies = [
"pgcli>=4.2.0",
"psycopg-binary>=3.0.0",
]
```
Then sync your environment:
```
uv sync
```

Additional troubleshooting steps (not uv-specific) if the issue persists:

1. Check Python Version:

```
$ python -V
```

Ensure Python is at least 3.9. The 'psycopg2-binary' installation may fail on older versions.

2. Environment Setup (if using a non-uv workflow):

```
$ conda create --name de-zoomcamp python=3.9
$ conda activate de-zoomcamp
```

3. Install Required Libraries:

```
pip install psycopg2-binary
pip install psycopg_binary
```

4. Upgrade pgcli:

```
pip install --upgrade pgcli
```

5. Install pgcli via Conda:

```
conda install -c conda-forge pgcli
```

If you still encounter an error like
```
ModuleNotFoundError: No module named 'psycopg2'
```
then try:
```
pip install psycopg2-binary
```
