---
id: 0d73dde53e
question: PGCLI - no pq wrapper available 
sort_order: 63
---

**Problem:**

```
ImportError: no pq wrapper available.
```

### Problem Details:

- Could not import `\dt`
- `opg 'c' implementation: No module named 'psycopg_c'`
- `couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary'`
- `couldn't import psycopg 'python' implementation: libpq library not found`

### Solution:

In your virtual environment, ensure you are in your working directory (e.g., pipeline).

Add psycopg binary using uv:

```bash
$ uv add "psycopg[binary]"
```

