---
id: fb43c209d9
question: How to set environment variable easily for any credentials
sort_order: 50
---

If you need to securely set up credentials for a project and intend to push it to a git repository, using an environment variable is a recommended option.

For example, for scripts like `web_to_gcs.py` or `git_csv_to_gcs.py`, you may need to set these variables:

- `GOOGLE_APPLICATION_CREDENTIALS`
- `GCP_GCS_BUCKET`

The easiest option to manage this is to use a `.env` file with [dotenv](https://pypi.org/project/python-dotenv/).

To install and utilize this package, follow these steps:

1. Install `python-dotenv`:

   ```bash
   pip install python-dotenv
   ```

2. Add the following code to inject these variables into your project:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Now you can access environment variables like GCP_GCS_BUCKET and GOOGLE_APPLICATION_CREDENTIALS
   credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
   BUCKET = os.environ.get("GCP_GCS_BUCKET")
   ```