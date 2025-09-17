---
course: data-engineering-zoomcamp
id: 5d8ffd5be5
question: Python - SQLALchemy - TypeError 'module' object is not callable
section: 'Module 1: Docker and Terraform'
sort_order: 1370
---

create_engine('postgresql://root:root@localhost:5432/ny_taxi')  I get the error "TypeError: 'module' object is not callable"

Solution:
conn_string = "postgresql+psycopg://root:root@localhost:5432/ny_taxi"
engine = create_engine(conn_string)

