---
id: 6435e27634
question: Ingestion: When attempting to use the provided quick script to load trip data into GCS, you receive error Access Denied from the S3 bucket
section: Module 4: analytics engineering with dbt
course: data-engineering-zoomcamp
sort_order: 2540
---

If the provided URL isn’t working for you (https://nyc-tlc.s3.amazonaws.com/trip+data/):

We can use the GitHub CLI to easily download the needed trip data from https://github.com/DataTalksClub/nyc-tlc-data, and manually upload to a GCS bucket.

Instructions on how to download the CLI here: https://github.com/cli/cli

Commands to use:

gh auth login

gh release list -R DataTalksClub/nyc-tlc-data

gh release download yellow -R DataTalksClub/nyc-tlc-data

gh release download green -R DataTalksClub/nyc-tlc-data

etc.

Now you can upload the files to a GCS bucket using the GUI.

