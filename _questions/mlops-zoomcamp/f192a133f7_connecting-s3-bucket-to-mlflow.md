---
course: mlops-zoomcamp
id: f192a133f7
question: Connecting s3 bucket to MLFLOW
section: 'Module 4: Deployment'
sort_order: 1700
---

Problem description. How can we connect s3 bucket to MLFLOW?

Solution: Use boto3 and AWS CLI to store access keys. The access keys are what will be used by boto3 (AWS' Python API tool) to connect with the AWS servers. If there are no Access Keys how can they make sure that they have the right to access this Bucket? Maybe you're a malicious actor (Hacker for ex). The keys must be present for boto3 to talk to the AWS servers and they will provide access to the Bucket if you possess the right permissions. You can always set the Bucket as public so anyone can access it, now you don't need access keys because AWS won't care.

Read more here:

Added by Akshit Miglani

