---
id: e5b8322bee
question: 'DBT: Error: No module named ''pytz'' while setting up dbt with docker'
sort_order: 44
---

Following dbt with [BigQuery on Docker readme.md](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/docker_setup/README.md), after running `docker-compose build` and `docker-compose run dbt-bq-dtc init`, you might encounter the error:

```
ModuleNotFoundError: No module named 'pytz'
```

Solution:

Add the following line in the Dockerfile under `FROM --platform=$build_for python:3.9.9-slim-bullseye as base`:

```bash
RUN python -m pip install --no-cache pytz
```