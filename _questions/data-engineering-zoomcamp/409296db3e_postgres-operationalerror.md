---
course: data-engineering-zoomcamp
id: 409296db3e
question: 'Postgres - OperationalError: (psycopg2.OperationalError) connection to
  server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed
  for user "root"'
section: 'Module 1: Docker and Terraform'
sort_order: 1190
---

This happens while uploading data via the connection in jupyter notebook

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

The port 5432 was taken by another postgres. You could already have installed Postgres in the past at the same port, so when you are trying to connect it does not reach docker, but the old Postgres installation instead. We are not connecting to the port in docker, but to the port on our machine. Substitute 5431 or whatever port you mapped to for port 5432. Another option is to remove the old Postgres installation if it is useless.

Also if this error is still persistent , kindly check if you have a service in windows running postgres. Stopping that service will resolve the issue

