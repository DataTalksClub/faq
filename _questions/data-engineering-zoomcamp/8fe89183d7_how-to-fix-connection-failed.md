---
course: data-engineering-zoomcamp
id: 8fe89183d7
question: 'How to fix “connection failed: connection to server at "127.0.0.1", port
  5432 failed” error when setting up Postgres connection in pgAdmin?'
section: 'Module 6: streaming with kafka'
sort_order: 4160
---

Instead of using “localhost” as the host name/address, try “postgres”, or “host.docker.internal” instead

Alternative Solution: For those having installed postgres locally and disabling persist data on postgres-container in docker i.e. volume: removed, remember to use postgres port other than 5432 (e.g. 5433 is usable). And for pgadmin host name/address, if localhost, postgres, and host.docker.internal is not working, you can use your own IPv4 Address which can be found in Windows OS via: Command Prompt > ipconfig > Under Wireless LAN adapter WiFi 2. E.g.:

IPv4 Address. . . . . . . . . . . : 192.168.0.148

