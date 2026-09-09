---
id: f067a2c8e6
question: 'Command aws ecr get-login --no-include-email returns “aws: error: argument
  operation: Invalid choice…”'
sort_order: 24
---

The error occurs because the `aws ecr get-login` command is deprecated.

Instead, use the following command to authenticate Docker to an ECR registry:

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
```

Replace `<your-region>` with your AWS region and `<your-account-id>` with your account ID.

If you have a default region configured, this variant needs no changes:

```bash
aws ecr get-login-password --region $(aws configure get region) | docker login --username AWS --password-stdin "$(aws sts get-caller-identity --query "Account" --output text).dkr.ecr.$(aws configure get region).amazonaws.com"
```