---
course: data-engineering-zoomcamp
id: b9cd2aaccb
question: 'PGCLI - connection failed: :1), port 5432 failed: could not receive data
  from server: Connection refused could not send SSL negotiation packet: Connection
  refused'
section: 'Module 1: Docker and Terraform'
sort_order: 1060
---

Change TO Socket

pgcli -h 127.0.0.1 -p 5432 -u root -d ny_taxi

pgcli -h 127.0.0.1 -p 5432 -u root -d ny_taxi

