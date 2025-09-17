---
course: machine-learning-zoomcamp
id: b612fa07ec
question: 'Command aws ecr get-login --no-include-email returns “aws: error: argument
  operation: Invalid choice…”'
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3640
---

As per AWS documentation:

[docs.aws.amazon.com](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)

You need to do: (change the fields in red)

aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com

Alternatively you can run the following command without changing anything given you have a default region configured

aws ecr get-login-password --region $(aws configure get region) | docker login --username AWS --password-stdin "$(aws sts get-caller-identity --query "Account" --output text).dkr.ecr.$(aws configure get region).amazonaws.com"

Added by Humberto Rodriguez

