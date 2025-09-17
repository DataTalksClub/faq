---
course: data-engineering-zoomcamp
id: df2ca336d5
question: 'DBT-Config ERROR on CLOUD IDE: No dbt_project.yml found at expected path'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2430
---

(Lower left Corner after setting all connections to BQ and Github)

14:48:39 Running dbt...

14:48:39 Encountered an error:

Runtime Error

No dbt_project.yml found at expected path /usr/src/develop/user-70471823426120/environment-70471823422561/repository-70471823410839/dbt_project.yml

Verify that each entry within packages.yml (and their transitive dependencies) contains a file named dbt_project.yml

Solution: Initialize a project through UI.

Importing git repo of an existing dbt project:

Please read through these details for doing it:

