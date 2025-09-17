---
id: ec6d89a462
question: Access Denied: Table yellow_tripdata: User does not have permission to query table yellow_tripdata, or perhaps it does not exist in location US.
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2980
---

![Image](images/data-engineering-zoomcamp/image_ee3efac5.png)

Database Error in model stg_yellow_tripdata (models/staging/stg_yellow_tripdata.sql)

Access Denied: Table taxi-rides-ny-339813-412521:trips_data_all.yellow_tripdata: User does not have permission to query table taxi-rides-ny-339813-412521:trips_data_all.yellow_tripdata, or perhaps it does not exist in location US.

compiled Code at target/run/taxi_rides_ny/models/staging/stg_yellow_tripdata.sql

In my case, I was set up in a different branch, so always check the branch you are working on. Change the 04-analytics-engineering/taxi_rides_ny/models/staging/schema.yml file in the

sources:

- name: staging

database: your_database_name

If this error will continue when running dbt job, As for changing the branch for your job, you can use the ‘Custom Branch’ settings in your dbt Cloud environment. This allows you to run your job on a different branch than the default one (usually main). To do this, you need to:

Go to an environment and select Settings to edit it

Select Only run on a custom branch in General settings

Enter the name of your custom branch (e.g. HW)

Click Save

