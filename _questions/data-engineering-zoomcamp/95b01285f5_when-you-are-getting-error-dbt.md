---
id: 95b01285f5
question: When You are getting error dbt_utils not found
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2620
---

You need to create packages.yml file in main project directory and add packages’ meta data:

packages:

- package: dbt-labs/dbt_utils

version: 0.8.0

After creating file run:

dbt deps

And hit enter.

