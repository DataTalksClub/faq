---
id: c6a6a991d8
question: PGCLI - running in a Docker container
sort_order: 6
---

If running pgcli locally causes issues or you do not want to install it on your machine, you can use it within a Docker container instead.

Below is the usage with values used in the course videos for:

- Network name (Docker network)
- Postgres-related variables for pgcli
- Hostname
- Username
- Port
- Database name

```bash
docker run -it --rm --network pg-network ai2ys/dockerized-pgcli:4.0.1
```

Then execute the following pgcli command:

```sql
pgcli -h pg-database -U root -p 5432 -d ny_taxi
```

You'll be prompted for the password for the user `root`.

Example Output:

```
Server: PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
Version: 4.0.1
Home: [pgcli.com](http://pgcli.com)
```

To list tables:

```sql
root@pg-database:ny_taxi> \dt

+--------+------------------+-------+-------+
| Schema | Name             | Type  | Owner |
|--------+------------------+-------+-------|
| public | yellow_taxi_data | table | root  |
+--------+------------------+-------+-------+

SELECT 1
Time: 0.009s
root@pg-database:ny_taxi>
```