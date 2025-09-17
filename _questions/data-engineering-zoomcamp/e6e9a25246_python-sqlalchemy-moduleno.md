---
course: data-engineering-zoomcamp
id: e6e9a25246
question: 'Python - SQLAlchemy - ModuleNotFoundError: No module named ''psycopg2''.'
section: 'Module 1: Docker and Terraform'
sort_order: 1380
---

Error raised during the jupyter notebook’s cell execution:

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi').

Solution: Need to install Python module “psycopg2”. Can be installed by Conda or pip.

