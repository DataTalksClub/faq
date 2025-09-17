---
course: mlops-zoomcamp
id: abb38848b5
question: How to destroy infrastructure created via GitHub Actions
section: 'Module 6: Best practices'
sort_order: 2370
---

Problem description

Infrastructure created in AWS with CD-Deploy Action needs to be destroyed

Solution description

From local:

terraform init -backend-config="key=mlops-zoomcamp-prod.tfstate" --reconfigure

terraform destroy --var-file vars/prod.tfvars

Added by Erick Calderin

