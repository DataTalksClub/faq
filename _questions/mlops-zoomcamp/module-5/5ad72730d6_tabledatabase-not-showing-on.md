---
id: 5ad72730d6
images:
- description: 'image #1'
  id: image_1
  path: images/mlops-zoomcamp/image_a92c0f4d.png
question: Table/database not showing on grafana dashboard
sort_order: 2090
---

Problem: for 5.4, when trying to create a new dashboard grafana does not list the ‘dummy_metrics’ table in the query tab.

Note: also change the datasource name other than PostgreSQL

Solution1: update the config/grafana_datasources.yaml to the following:

# list of datasources to insert/update

# available in the database

datasources:

- name: NewPostgreSQL

type: postgres

url: db:5432

user: postgres

secureJsonData:

password: 'example'

jsonData:

sslmode: 'disable'

database: test

Solution 2: Utilise the Code option rather than the Builder option and load the data in using your own SQL queries. See screenshot below (box highlight in red). Tip, if you write your FROM statement first the SELECT options are able to be done through auto-complete too.

<{IMAGE:image_1}>

Answered by  Anuj Panthri, added by Andrea Nicolas, edit by Marcus Leiwe

