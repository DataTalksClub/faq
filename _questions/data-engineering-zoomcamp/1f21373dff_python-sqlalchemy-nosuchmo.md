---
course: data-engineering-zoomcamp
id: 1f21373dff
question: 'Python - SQLAlchemy - NoSuchModuleError: Can''t load plugin: sqlalchemy.dialects:postgresql.psycopg'
section: 'Module 1: Docker and Terraform'
sort_order: 1390
---

Error raised during the jupyter notebook’s cell execution:

conn_string = "postgresql+psycopg://root:root@localhost:5432/ny_taxi"

engine = create_engine(conn_string)

Solution: We had a scenario of a virtualenv (created by Pycharm) being run on top of another virtual env (on conda). Solution was:

to get rid of the .venv

create a brand new virtualenv with conda conda create -n pyingest python=3.12

install the required dependencies pip install pandas sqlalchemy psycopg2-binary jupyterlab

And re-execute the code.

For psycopg2, the connection string should be:

postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}

Reference - Kayla Tinker 1/14/25

