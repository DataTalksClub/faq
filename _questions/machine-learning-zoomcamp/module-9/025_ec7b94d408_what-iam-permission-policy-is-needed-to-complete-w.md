---
id: ec7b94d408
question: 'What IAM permission policy is needed to complete Week 9: Serverless?'
sort_order: 25
---

1. **Sign in to the AWS Console**: Log in to the AWS Console.

2. **Navigate to IAM**: Go to the IAM service by clicking on "Services" in the top left corner and selecting "IAM" under the "Security, Identity, & Compliance" section.

3. **Create a new policy**:
   - In the left navigation pane, select "Policies" and click on "Create policy."

4. **Select the service and actions**:
   - Click on "JSON" and copy and paste the JSON policy for the specific ECR actions.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "ecr:CreateRepository",
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:InitiateLayerUpload",
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload",
        "ecr:PutImage"
      ],
      "Resource": "*"
    }
  ]
}
```

5. **Review and create the policy**:
   - Click on "Review policy."
   - Provide a name and description for the policy.
   - Click on "Create policy."

**Error Resolution**

If you encounter the following error:

```bash
ERROR: failed to solve: public.ecr.aws/lambda/python:3.10: error getting credentials - err: exec: "docker-credential-desktop.exe": executable file not found in $PATH, out: ``
```

- **Solution**: Delete the file `~/.docker/config.json`