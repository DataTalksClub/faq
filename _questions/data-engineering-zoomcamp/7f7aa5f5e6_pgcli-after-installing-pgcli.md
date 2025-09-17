---
id: 7f7aa5f5e6
question: PGCLI - After installing PGCLI and checking with pgcli -- help we get the error: ImportError: no pq wrapper available
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1180
---

The error persists because the psycopg library cannot find the required libpq library. Ensure the required PostgreSQL client library is installed:
	sudo apt install libpq-dev
Rebuild psycopg 
	pip uninstall psycopg psycopg_binary psycopg_c -y
	pip install psycopg --no-binary psycopg
The issue should be resolved by now. However, even after these steps you get the error:
ModuleNotFoundError: No module named 'psycopg2'
Then run the following:
	pip install psycopg2-binary

