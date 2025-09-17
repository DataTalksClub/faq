---
course: data-engineering-zoomcamp
id: fb43c209d9
question: How to set environment variable easily for any credentials
section: 'Module 4: analytics engineering with dbt'
sort_order: 3140
---

If you have to securely put your credentials for a project and, probably, push it to a git repository then the best option is to use an environment variable

For example for web_to_gcs.py or git_csv_to_gcs.py we have to set these variables:

GOOGLE_APPLICATION_CREDENTIALS

GCP_GCS_BUCKET

The easises option to do it  is to use .env  ().

Install it and add a few lines of code that inject these variables for your project
pip install python-dotenv

from dotenv import load_dotenv

import os

# Load environment variables from .env file

load_dotenv()

# Now you can access environment variables like GCP_GCS_BUCKET and GOOGLE_APPLICATION_CREDENTIALS

credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

BUCKET = os.environ.get("GCP_GCS_BUCKET")

