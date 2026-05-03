---
id: a31defac51
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_d2b29adb.png
question: Why do we need the Staging dataset?
sort_order: 22
---

<{IMAGE:image_1}>

Staging, as the name suggests, acts as an intermediary between raw datasets and the final fact and dimension tables. It helps in transforming raw data into a more usable format. In staging, datasets are typically materialized as views rather than tables.

In the project, you focus on creating production and `dbt_name + trips_data_all`; the staging dataset serves its role behind the scenes.