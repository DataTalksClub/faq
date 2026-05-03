---
id: fa8cbc8f40
question: 'Terraform: google provider requires credentials.'
sort_order: 12
---

To ensure the sensitivity of the credentials file, use the following configuration:

```hcl
provider "google" {
  project     = var.projectId
  credentials = file("${var.gcpkey}")
  #region      = var.region
  zone = var.zone
}
```