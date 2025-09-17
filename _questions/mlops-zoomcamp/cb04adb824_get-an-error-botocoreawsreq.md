---
id: cb04adb824
question: Get an error “<botocore.awsrequest.AWSRequest object at 0x7fbaf2666280>” after running an AWS CLI command
section: Module 6: Best practices
course: mlops-zoomcamp
sort_order: 2240
---

When executing an AWS CLI command (e.g., aws s3 ls), you can get the error <botocore.awsrequest.AWSRequest object at 0x7fbaf2666280>.

To fix it, simply set the AWS CLI environment variables:

export AWS_DEFAULT_REGION=eu-west-1

export AWS_ACCESS_KEY_ID=foobar

export AWS_SECRET_ACCESS_KEY=foobar

Their value is not important; anything would be ok.

Added by Giovanni Pecoraro

