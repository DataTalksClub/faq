---
id: 4b65d5542d
question: 'OperationalError when running python prep.py: psycopg2. OperationalError:
  could not translate host name "postgres" to address: No such host is known. How
  do I fix this issue?'
sort_order: 2
---

To resolve this error, update the `.env` file:

- Change the `POSTGRES_HOST` variable to `localhost`.

```ini
POSTGRES_HOST=localhost
```
