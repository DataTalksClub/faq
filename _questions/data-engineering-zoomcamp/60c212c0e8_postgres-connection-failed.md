---
course: data-engineering-zoomcamp
id: 60c212c0e8
question: 'Postgres - connection failed: connection to server at "127.0.0.1", port
  5432 failed: FATAL:  password authentication failed for user "root"'
section: 'Module 1: Docker and Terraform'
sort_order: 1200
---

check that the port was properly forwarded. If 5432 is being used, kill the process:

sudo lsof -i :5432

sudo kill -9 PID

Windows users:
Found that my issue was related to PostgresSQL running locally on my machine and that pgAdmin4 was using my 5432 port.

To stop this process:

1. Press Win + R to open the Run dialog.

2. Type services.msc and press Enter.

3. In the Services window, scroll down and look for a service with a name like PostgreSQL, postgresql-x64-13, or similar (the exact name depends on your PostgreSQL version).

4. Right-click the PostgreSQL service and select Stop.

