---
id: f831690b89
question: How do I log in to AWS ECR from the terminal using Docker?
sort_order: 1
---

The older `aws ecr get-login --no-include-email` command is deprecated. Use:

```bash
aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin <ACCOUNTID>.dkr.ecr.<REGION>.amazonaws.com
```

Make sure you specify the correct AWS region where your ECR repository is located (e.g., `us-west-1`). If the region is incorrect or not set properly, the login will fail with a `400 Bad Request` error — which doesn't clearly indicate the region is the issue.
