---
id: ec7b94d408
question: What IAM permission policy is needed to complete Week 9: Serverless?
section: 9. Serverless Deep Learning
course: machine-learning-zoomcamp
sort_order: 3300
---

Sign in to the AWS Console: Log in to the AWS Console.

Navigate to IAM: Go to the IAM service by clicking on "Services" in the top left corner and selecting "IAM" under the "Security, Identity, & Compliance" section.

Create a new policy: In the left navigation pane, select "Policies" and click on "Create policy."

Select the service and actions:

Click on "JSON" and copy and paste the JSON policy you provided earlier for the specific ECR actions.

Review and create the policy:

Click on "Review policy."

Provide a name and description for the policy.

Click on "Create policy."

JSON policy:

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

Added by: Daniel Muñoz-Viveros

ERROR: failed to solve: public.ecr.aws/lambda/python:3.10: error getting credentials - err: exec: "docker-credential-desktop.exe": executable file not found in $PATH, out: ``

(WSL2 system)

Solved: Delete the file ~/.docker/config.json

Yishan Zhan

