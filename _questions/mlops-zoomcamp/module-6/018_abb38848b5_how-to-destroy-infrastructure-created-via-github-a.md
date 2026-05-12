---
id: abb38848b5
question: How to destroy infrastructure created via GitHub Actions
sort_order: 18
---

Infrastructure created in AWS with CD-Deploy Action needs to be destroyed.

To destroy the infrastructure from local:

```bash
terraform init -backend-config="key=mlops-zoomcamp-prod.tfstate" --reconfigure
```

```bash
terraform destroy --var-file vars/prod.tfvars
```