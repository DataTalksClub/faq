---
id: 00b11da94b
question: 'Going further with Google Cloud Platform: Load and save data to GCS'
sort_order: 13
---

There is a possibility to load and store data in a Google Cloud Storage bucket. To do that, authenticate through the IDE you are using and allow read and write access to a GCS bucket:

1. **Authenticate gsutil with your GCP account:**
   ```bash
   gsutil config
   ```

2. **Upload the data to your GCS bucket:**
   ```bash
   gsutil cp path/to/local/data gs://your-bucket-name
   ```

3. **Create a service account and manage permissions:**
   - In the GCP Console, go to "IAM & Admin," then "Service accounts."
   - Create a new service account, grant it permissions (e.g., "Storage Object Admin" for GCS access), and generate a JSON key file.

4. **Install the Google Cloud SDK:**
   [Google Cloud SDK Installation Guide](https://cloud.google.com/sdk/docs/install)

5. **Authenticate the SDK with your GCP account:**
   ```bash
   gcloud auth login
   ```

6. **Set your GCP project:**
   ```bash
   gcloud config set project YOUR_GCP_PROJECT_ID
   ```

7. **Install the Google Cloud Storage library:**
   ```bash
   !pip install google-cloud-storage
   ```

**Example Script**

Here's how to load a CSV file from Google Cloud Storage into a pandas DataFrame:

```python
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
```

You can directly save output data by setting the output file name to your desired GCS URI.