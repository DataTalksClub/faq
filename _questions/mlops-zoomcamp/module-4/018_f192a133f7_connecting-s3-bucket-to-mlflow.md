---
id: f192a133f7
question: Connecting s3 bucket to MLFLOW
sort_order: 18
---

How can we connect an S3 bucket to MLflow?

To connect an S3 bucket to MLflow, use `boto3` and AWS CLI to store access keys. These access keys allow `boto3` (AWS' Python API tool) to authenticate and connect with AWS servers. Without access keys, access to the bucket cannot be verified, which could prevent connection attempts by unauthorized individuals.

Steps:

1. **Ensure Access Keys are Available:**
   - Access keys are essential for `boto3` to communicate with AWS servers securely.
   - They ensure that only authorized users with the correct permissions can access the bucket.

2. **Set Bucket as Public (Optional):**
   - Alternatively, you can set the bucket to public access.
   - In this case, access keys are not needed as anyone can access the bucket without authentication.

For more detailed information on credentials management, refer to the official documentation:
[https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)