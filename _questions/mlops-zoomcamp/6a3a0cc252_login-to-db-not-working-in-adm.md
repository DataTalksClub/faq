---
id: 6a3a0cc252
question: Login to DB not working in Adminer UI even after right DB, user and password.
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2170
---

Problem: In adminer ui Adminer access is not working even after right DB user and password

(It wasn't for me) Adminer simply does not respond and does not show DB details

![Image](images/mlops-zoomcamp/image_c66aba56.png)

Solution: Try accessing DB from command line via psql

You can quickly install psql via sudo apt etc

Here is the example

(base) cpl@inpne-ed-lab003:~$ psql -h localhost -p 5432 -U postgres

Password for user postgres:

psql (14.12 (Ubuntu 14.12-0ubuntu0.22.04.1), server 16.4 (Debian 16.4-1.pgdg120+1))

WARNING: psql major version 14, server major version 16.

Some psql features might not work.

Type "help" for help.

postgres=# \l

List of databases

Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges

-----------+----------+----------+------------+------------+-----------------------

postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |

template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +

|          |          |            |            | postgres=CTc/postgres

template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +

|          |          |            |            | postgres=CTc/postgres

test      | postgres | UTF8     | en_US.utf8 | en_US.utf8 |

(4 rows)

Added by Nilesh Arte

