---
id: e5b8322bee
question: DBT - Error: No module named 'pytz' while setting up dbt with docker
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 3040
---

Following dbt with , after `docker-compose build` and `docker-compose run dbt-bq-dtc init`, encountered error `ModuleNotFoundError: No module named 'pytz'`

Solution:

Add `RUN python -m pip install --no-cache pytz` in the Dockerfile under `FROM --platform=$build_for python:3.9.9-slim-bullseye as base`

