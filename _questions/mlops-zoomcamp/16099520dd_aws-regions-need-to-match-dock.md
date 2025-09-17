---
course: mlops-zoomcamp
id: 16099520dd
question: AWS regions need to match docker-compose
section: 'Module 6: Best practices'
sort_order: 2350
---

Problem description

If you are having problems with the integration tests and kinesis double check that your aws regions match on the docker-compose and local config. Otherwise you will be creating a stream in the wrong region

Solution description

For example set ~/.aws/config region = us-east-1 and the docker-compose.yaml - AWS_DEFAULT_REGION=us-east-1

Added by Quinn Avila

