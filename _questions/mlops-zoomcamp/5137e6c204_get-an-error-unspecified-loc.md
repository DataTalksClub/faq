---
id: 5137e6c204
question: Get an error ‘ unspecified location constraint is incompatible ’
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2230
---

You may get an error while creating a bucket with localstack and the boto3 client:

botocore.exceptions.ClientError: An error occurred (IllegalLocationConstraintException) when calling the CreateBucket operation: The unspecified location constraint is incompatible for the region specific endpoint this request was sent to.

To fix this, instead of creating a bucket via

s3_client.create_bucket(Bucket='nyc-duration')

Create it with

s3_client.create_bucket(Bucket='nyc-duration', CreateBucketConfiguration={

'LocationConstraint': AWS_DEFAULT_REGION})

yam

Added by M

