---
id: 8fe89183d7
question: 'How to fix “connection failed: connection to server at "127.0.0.1", port
  5432 failed” error when setting up Postgres connection in pgAdmin?'
sort_order: 29
---

Instead of using “localhost” as the host name/address, try “postgres”, or “host.docker.internal” instead.

Alternative Solution:

- If you have installed Postgres locally and disabled persist data on the Postgres container in Docker (i.e., volume: removed), use a Postgres port other than 5432, such as 5433.
- For the pgAdmin host name/address, if 'localhost', 'postgres', or 'host.docker.internal' are not working, you can use your own IPv4 Address.

  To find your IPv4 Address on Windows OS:
  
  1. Open Command Prompt.
  2. Run the command:
     
     ```bash
     ipconfig
     ```
  
  3. Look under Wireless LAN adapter WiFi 2 for the IPv4 Address. For example:

     ```text
     IPv4 Address. . . . . . . . . . . : 192.168.0.148
     ```