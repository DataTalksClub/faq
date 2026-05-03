---
id: 64d0d03a6f
question: 'Terraform Error 412: Request violates constraint ''constraints/storage.uniformBucketLevelAccess'',
  conditionNotMet'
sort_order: 14
---

Cause:
The error occurs because the Google Cloud Storage bucket is under a constraint that requires Uniform Bucket-Level Access (UBLA) to be enabled. If UBLA is not enabled, Terraform apply can fail with 412.

Fix:
Enable UBLA in the google_storage_bucket resource by setting uniform_bucket_level_access = true.

Example:

```hcl
resource "google_storage_bucket" "demo-bucket" {
  name = "demo-bucket"

  uniform_bucket_level_access = true
}
```

Notes:
- Add this line to the google_storage_bucket resource for the affected bucket.
- After applying, re-run terraform apply to confirm the error is resolved.
