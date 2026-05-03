---
id: 6435e27634
question: 'Ingestion: When attempting to use the provided quick script to load trip
  data into GCS, you receive error Access Denied from the S3 bucket'
sort_order: 12
---

If the provided URL isn’t working for you ([nyc-tlc.s3.amazonaws.com](https://nyc-tlc.s3.amazonaws.com/trip+data)/):

We can use the GitHub CLI to easily download the needed trip data from [GitHub](https://github.com/DataTalksClub/nyc-tlc-data) and manually upload to a GCS bucket.

Instructions on how to download the CLI here: [GitHub](https://github.com/cli/cli)

Commands to use:

```bash
gh auth login

gh release list -R DataTalksClub/nyc-tlc-data

gh release download yellow -R DataTalksClub/nyc-tlc-data

gh release download green -R DataTalksClub/nyc-tlc-data
```

Now you can upload the files to a GCS bucket using the GUI.