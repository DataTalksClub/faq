---
course: mlops-zoomcamp
id: 74974bf558
question: 'aws.exe: error: argument operation: Invalid choice — Docker can not login
  to ECR.'
section: 'Module 4: Deployment'
sort_order: 1550
---

Windows with AWS CLI already installed

AWS CLI version:

aws-cli/2.4.24 Python/3.8.8 Windows/10 exe/AMD64 prompt/off

Executing

$(aws ecr get-login --no-include-email)

shows error

aws.exe: error: argument operation: Invalid choice, valid choices are…

Use this command instead. More info here:

[https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html)

aws ecr get-login-password \

--region <region> \

| docker login \

--username AWS \

--password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

Added by MarcosMJD

