---
id: b612fa07ec
question: 'Command aws ecr get-login --no-include-email returns "aws: error: argument
  operation: Invalid choice…"'
sort_order: 25
---

As per AWS documentation:

You need to execute the following command:

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

- Replace `<region>` and `<aws_account_id>` with your specific details.

Alternatively, you can run the following command without changing anything, given you have a default region configured:

```bash
aws ecr get-login-password --region $(aws configure get region) | docker login --username AWS --password-stdin "$(aws sts get-caller-identity --query "Account" --output text).dkr.ecr.$(aws configure get region).amazonaws.com"
```