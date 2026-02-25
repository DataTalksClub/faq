---
id: 7f7aa5f5e6
question: 'PGCLI - ImportError: no pq wrapper available (including uv package manager
  fixes)'
sort_order: 71
---

This error occurs because psycopg cannot find the PostgreSQL client library (libpq). The simplest solution with uv is to install the binary version of psycopg, which bundles the required library.

**Solution 1:** Add psycopg-binary (Recommended)

```bash
uv add psycopg-binary
uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```

**Solution 2:** Manually edit `pyproject.toml`

```toml
[project]
dependencies = [
    "pgcli>=4.2.0",
    "psycopg-binary>=3.0.0",
]
```

Then sync your environment:

```bash
uv sync
```

**Additional troubleshooting steps** (not uv-specific) if the issue persists:

1. Check Python version — ensure Python is at least 3.9:

    ```bash
    python -V
    ```

2. Environment setup (if using a non-uv workflow):

    ```bash
    conda create --name de-zoomcamp python=3.9
    conda activate de-zoomcamp
    ```

3. Install required libraries:

    ```bash
    pip install psycopg2-binary
    pip install psycopg_binary
    ```

4. Upgrade pgcli:

    ```bash
    pip install --upgrade pgcli
    ```

5. Install pgcli via Conda:

    ```bash
    conda install -c conda-forge pgcli
    ```

If you still encounter `ModuleNotFoundError: No module named 'psycopg2'`, try:

```bash
pip install psycopg2-binary
```
