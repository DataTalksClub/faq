---
id: 74974bf558
question: 'Docker: aws.exe: error: argument operation: Invalid choice — Docker can
  not login to ECR.'
sort_order: 2
---

When using AWS CLI on Windows, you might encounter the following error:

```
aws.exe: error: argument operation: Invalid choice
```

1. Check your AWS CLI version. For example:
   
   ```
   aws-cli/2.4.24 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
   ```

2. Instead of using the outdated command, use the updated command provided by AWS:

   ```bash
   aws ecr get-login-password \
   --region <region> \
   | docker login \
   --username AWS \
   --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
   ```

3. Refer to the official AWS documentation for additional details: [AWS CLI ECR Login Password](https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login-password.html)

Ensure that you replace `<region>` and `<aws_account_id>` with your specific values.