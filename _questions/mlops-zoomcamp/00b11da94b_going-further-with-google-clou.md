---
id: 00b11da94b
question: Going further with Google Cloud Platform (load and save data to GCS)
section: Module 4: Deployment
course: mlops-zoomcamp
sort_order: 1650
---

There is a possibility to load and store the data in a Google Cloud Storage bucket. To do that, we will need to authenticate through the IDE we are using (for example github Codespaces) and allow the read and write from/to a GCS bucket:

Authenticate gsutil with your GCP account: gsutil config

Upload the data to your GCS bucket: gsutil cp path/to/local/data gs://your-bucket-name

In the GCP Console, go to the "IAM & Admin" section, then "Service accounts."

Create a new service account, grant it the necessary permissions (e.g., "Storage Object Admin" for GCS access), and generate a JSON key file.

Install the Google Cloud SDK:

Authenticate the SDK with your GCP account: gcloud auth login

Set the project: gcloud config set project YOUR_GCP_PROJECT_ID

Install google cloud storage library (you can do it with a pip install directly in your notebook): !pip install google-cloud-storage

Example script on how to do it to load a file from a csv to a pandas df:

from google.cloud import storage

import pandas as pd

# Set up the storage client with the service account key

storage_client = storage.Client.from_service_account_json('path/to/service-account-key.json')

# Get the GCS bucket

bucket = storage_client.get_bucket('your-bucket-name')

# List the contents of the bucket

blobs = bucket.list_blobs()

for blob in blobs:

print(blob.name)

# Load a CSV file from the bucket into a pandas DataFrame

csv_blob = bucket.blob('path/to/csv/in/bucket.csv')

df = pd.read_csv(csv_blob.download_as_string())

You can directly save output data by setting the output file name to your desired file gsutil uri.

Added by Mélanie Fouesnard

