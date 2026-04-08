---
id: 79792b53fc
question: Why does my Bruin seed asset fail with a timeout error related to ingestr
  or duckdb installation?
sort_order: 6
---

### Summary
Bruin seed assets can fail with a timeout when Bruin dynamically installs the ingestr package and the DuckDB wheel during execution. If the network is slow or unstable, the installer steps may time out, causing the pipeline to fail.

### Cause
- Bruin uses uv to install required dependencies at run time.
- The ingestr package and the DuckDB wheel are downloaded during seed asset execution.
- Slow or unreliable network connectivity can cause installation to exceed the timeout.

### Solutions
1. Increase the HTTP timeout for uv

```bash
export UV_HTTP_TIMEOUT=120
```

2. Ensure stable network connectivity during seed execution.

3. For small static lookup tables, replace the seed asset with a SQL asset using a VALUES clause to avoid dynamic dependency installation.

```sql
SELECT * FROM (VALUES ('A'), ('B'), ('C')) AS t(col);
```

### Notes
- Using SQL VALUES can provide more deterministic local execution when the lookup table is small and static.
- If you frequently depend on large non-static datasets, consider pre-bundling or caching dependencies to reduce runtime installation time.
