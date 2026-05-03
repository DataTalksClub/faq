---
id: 26ff32cb35
question: 'SQLAlchemy / psycopg: ImportError or NoSuchModuleError when calling create_engine'
sort_order: 19
---

Symptoms when running `from sqlalchemy import create_engine` in a notebook:

```
ImportError: cannot import name 'TypeAliasType' from 'typing_extensions'
ModuleNotFoundError: No module named 'psycopg2'
TypeError: 'module' object is not callable
NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgresql.psycopg
```

These all come from a few related causes.

## Missing or out-of-date `typing_extensions`

```
ImportError: cannot import name 'TypeAliasType' from 'typing_extensions'
```

Upgrade to 4.6+:

```bash
pip install --upgrade typing_extensions
```

## Missing the Postgres driver

```
ModuleNotFoundError: No module named 'psycopg2'
```

Install one of the binary distributions (avoids needing libpq dev headers):

```bash
pip install psycopg2-binary
# or, for SQLAlchemy 2.x with psycopg 3:
pip install "psycopg[binary]"
```

If `pip install psycopg2` fails with `pg_config not found`, you don't have libpq dev headers installed — use `psycopg2-binary` (or, on Mac, `brew install postgresql`).

## Connection-string dialect mismatch

`create_engine('postgresql://...')` works with both psycopg2 and psycopg, but to be explicit:

```python
# psycopg2 (most common)
"postgresql+psycopg2://root:root@localhost:5432/ny_taxi"

# psycopg (v3)
"postgresql+psycopg://root:root@localhost:5432/ny_taxi"
```

If you see `NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgresql.psycopg`, your installed psycopg version doesn't match the dialect string — install the matching driver or change the URL prefix.

## `'module' object is not callable`

You probably did `import sqlalchemy` and then called `sqlalchemy(...)` instead of `sqlalchemy.create_engine(...)`. Fix:

```python
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg://root:root@localhost:5432/ny_taxi")
```

## Stacked virtual environments

If you've nested virtualenvs (for example a PyCharm-generated `.venv` inside a project that already had its own venv), imports may resolve from a different env than you think. Cleanest fix: `rm -rf .venv`, create a single venv with `uv venv` (or `python -m venv`), and install dependencies there.
