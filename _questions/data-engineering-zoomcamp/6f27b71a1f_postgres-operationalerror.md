---
course: data-engineering-zoomcamp
id: 6f27b71a1f
question: 'Postgres - OperationalError: (psycopg2.OperationalError) connection to
  server at "localhost" (::1), port 5432 failed: FATAL:  database "ny_taxi" does not
  exist'
section: 'Module 1: Docker and Terraform'
sort_order: 1220
---

~\anaconda3\lib\site-packages\psycopg2\__init__.py in connect(dsn, connection_factory, cursor_factory, **kwargs)

120

121     dsn = _ext.make_dsn(dsn, **kwargs)

--> 122     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)

123     if cursor_factory is not None:

124         conn.cursor_factory = cursor_factory

OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  database "ny_taxi" does not exist

Make sure postgres is running. You can check that by running `docker ps`

✅Solution: If you have postgres software installed on your computer before now, build your instance on a different port like 8080 instead of 5432

