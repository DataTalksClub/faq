---
course: data-engineering-zoomcamp
id: 04f55d5846
question: 'BigQuery adapter: 404 Not found: Dataset was not found in location europe-west6'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2720
---

Go to Account settings >> Project >> Analytics >> Click on your connection >> go all the way down to Location and type in the GCP location just as displayed in GCP (e.g. europe-west6). You might need to reupload your GCP key.

Delete your dataset in GBQ

Rebuild project: dbt build

Newly built dataset should be in the correct location

