---
id: c180431de3
question: DBT Cloud production error: prod dataset not available in location EU
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2440
---

Problem: I am trying to deploy my DBT  models to production, using DBT Cloud. The data should live in BigQuery.  The dataset location is EU.  However, when I am running the model in production, a prod dataset is being create in BigQuery with a location US and the dbt invoke build is failing giving me "ERROR 404: porject.dataset:prod not available in location EU". I tried different ways to fix this. I am not sure if there is a more simple solution then creating my project or buckets in location US. Hope anyone can help here.

Note: Everything is working fine in development mode, the issue is just happening when scheduling and running job in production

Solution: I created the prod dataset manually in BQ and specified EU, then I ran the job.

