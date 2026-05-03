---
id: 06c61761df
question: "GCP: How do I create a service account key when 'service account key creation is disabled'?"
sort_order: 21
---

This error occurs when your organization has a policy that disables service account key creation. You can disable this policy using either the GCP Console or gcloud CLI.

### Option 1: Using GCP Console

1. Go to the [IAM dashboard](https://console.cloud.google.com/iam-admin/iam) (IAM & Admin > IAM)
2. Press Ctrl + O and make sure you select your organization
3. Click the "Edit Principal" button (pencil icon) next to your account
4. Search for "Organization Policy Administrator" role, add it and click save
5. On the left sidebar, go to [Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)
6. Look for the policy named "Disable service account key creation" that is active and select it
7. Click on "Manage policy" then click on the drop down that says "Enforced", set it to "Off"
8. Click "Done" and then the blue "Set policy" button

### Option 2: Using gcloud CLI

```bash
# Get your organization ID
gcloud organizations list

# Get your account email
gcloud auth list

# Add policy admin role if needed
gcloud organizations add-iam-policy-binding <ORGANIZATION_ID> \
  --member="user:<YOUR_ACCOUNT_EMAIL>" \
  --role="roles/orgpolicy.policyAdmin"

# Delete the policy
gcloud org-policies delete iam.disableServiceAccountKeyCreation \
  --organization=<ORGANIZATION_ID>
```

Reference: [GCP Organization Policies](https://cloud.google.com/resource-manager/docs/secure-by-default-organizations#disable_organization_policies)
