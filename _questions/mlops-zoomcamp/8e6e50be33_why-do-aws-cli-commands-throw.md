---
id: 8e6e50be33
question: Why do aws cli commands throw <botocore.awsrequest.AWSRequest object at 0x74c89c3562d0> type messages when listing or creating aws s3 buckets with localstack ?
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2340
---

If you encounter such messages when you try to list your aws s3 buckets for example (aws --endpoint-url=http://localhost:4566 s3 ls), you can try to configure AWS by setting up the same region, access key and secret key as the ones that appear in your docker-compose file.

After installing the aws cli, make sure you configure it in your terminal by entering this command line : aws configure

It will ask for:

AWS Access Key ID [None]: abc (example)

AWS Secret Access Key [None]: xyz (example)

Default region name [None]: eu-west-1 (example)

Added by Mélanie Fouesnard

