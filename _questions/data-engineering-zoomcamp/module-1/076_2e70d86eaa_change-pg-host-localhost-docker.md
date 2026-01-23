---
id: 2e70d86eaa
question: 'OperationalError: connection to server at ''localhost'' failed in ingest_script.py
  when running with --pg-host; how to fix by using pgdatabase?'
sort_order: 76
---

To fix the OperationalError when the ingest_script.py connects to PostgreSQL, ensure the database host in the script matches the Docker host name you pass at runtime.

- In ingest_script.py, locate the DB host setting:
  `pg_host = "localhost"`

- Change it to:
  `pg_host = "pgdatabase"`

- If you started the container with --pg-host=pgdatabase, the host inside the script must be pgdatabase so the connection is directed to the correct container/service.

- After updating, rerun the container with --pg-host=pgdatabase (and ensure the Postgres service is reachable under that host name in the Docker network).