---
course: data-engineering-zoomcamp
id: 0f6e2d3813
question: 'How do I solve the Dbt Cloud error: prod was not found in location?'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2450
---

You might get this error while trying to run dbt in production aftering following the instructions in the video ‘DE Zoomcamp 4.4.1 - Deployment Using dbt Cloud (Alternative A’):
Database Error in model stg_yellow_tripdata (models/staging/stg_yellow_tripdata.sql)
Not found: Dataset module-4-analytics-eng:prod was not found in location europe-west10

This error is easily solved. There are two solutions  to solve this issue:

Solution #1: Matching the dataset's data location with the source dataset

Set your ‘prod’ dataset's data location to match the data location of your ‘trips_data_all’ dataset's data location (in BigQuery). Running dbt in production works for the  instructor, because her ‘ prod’ is in the same region as her source data. Since your ‘trips_data_all’ is in europe-west10 (or anything else besides US), your prod needs to be there too; not US (which is a default setting when dbt creates a dataset for you in BigQuery).

Solution #2: Changing the dataset to <development dataset>

Go into your dbt production environment settings:
1. Go to: Deploy / Environments / Production (your production environment) / Settings
2. Now look at the Deployment credentials. There is an input field here called Dataset. The input of ‘prod’ is likely in here.
3. Replace ‘prod’ with the name of the Dataset that you worked with while in development (before moving to Production). This is the Dataset name inside your BigQuery where you successfully ran ‘dbt debug’ and ‘dbt build’ with.
4. After saving, you are ready to rerun your Job!

