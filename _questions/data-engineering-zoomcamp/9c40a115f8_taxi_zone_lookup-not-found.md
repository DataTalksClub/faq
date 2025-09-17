---
course: data-engineering-zoomcamp
id: 9c40a115f8
question: ‘taxi_zone_lookup’ not found
section: 'Module 4: analytics engineering with dbt'
sort_order: 2880
---

Check the .gitignore file and make sure you don’t have *.csv in it

Dbt error 404 was not found in location

My specific error:
Runtime Error in rpc request (from remote system.sql) 404 Not found: Table dtc-de-0315:trips_data_all.green_tripdata_partitioned was not found in location europe-west6 Location: europe-west6 Job ID: 168ee9bd-07cd-4ca4-9ee0-4f6b0f33897c

Make sure all of your datasets have the correct region and not a generalised region:
Europe-west6 as opposed to EU

Match this in dbt settings:
dbt -> projects -> optional settings -> manually set location to match

