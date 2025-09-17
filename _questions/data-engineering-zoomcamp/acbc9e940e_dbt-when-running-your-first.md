---
course: data-engineering-zoomcamp
id: acbc9e940e
question: 'DBT - When running your first dbt model, if it fails with an error:'
section: 'Module 4: analytics engineering with dbt'
sort_order: 2590
---

404 Not found: Dataset was not found in location US

404 Not found: Dataset eighth-zenith-372015:trip_data_all was not found in location us-west1

R: Go to BigQuery, and check the location of BOTH

The source dataset (trips_data_all), and

The schema you’re trying to write to (name should be 	dbt_<first initial><last name> (if you didn’t change the default settings at the end when setting up your project))

Likely, your source data will be in your region, but the write location will be a multi-regional location (US in this example). Delete these datasets, and recreate them with your specified region and the correct naming format.

Alternatively, instead of removing datasets, you can specify the single-region location you are using. E.g. instead of ‘location: US’, specify the region, so ‘location: US-east1’. See  for more detail. Additionally please see

In DBT cloud you can actually specify the location using the following steps:

GPo to your profile page (top right drop-down --> profile)

Then go to under Credentials --> Analytics (you may have customised this name)

Click on Bigquery >

Hit Edit

Update your location, you may need to re-upload your service account JSON to re-fetch your private key, and save. (NOTE: be sure to exactly copy the region BigQuery specifies your dataset is in.)

