---
id: f291e8d311
question: 'Postgres: bind: address already in use'
sort_order: 9
---

### Issue

When attempting to start the Docker Postgres container, you may encounter the error message:

```
Error - postgres port is already in use.
```

### Solutions

#### Option 1: Identify and Stop the Service

1. Determine which service is using the port by running:
   
   ```bash
   sudo lsof -i :5432
   ```
   
2. Stop the service that is using the port:
   
   ```bash
   sudo service postgresql stop
   ```

#### Option 2: Map to a Different Port

For a more long-term solution, consider mapping to a different port:

- Map local port 5433 to container port 5432 in your Docker configuration (`Dockerfile` or `docker-compose.yml`).
- If using a VM, ensure that port 5433 is forwarded in the host machine configuration.

This approach prevents conflicts and allows the Docker Postgres container to run without interruption.