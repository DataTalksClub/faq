---
id: f57e5cb1f4
question: "dbt Cloud: Connecting to BigQuery via Workload Identity Federation won't work — how to fix it?"
sort_order: 62
---

When setting up a dbt Cloud connection to BigQuery, you might try using **Workload Identity Federation (WIF)** instead of a JSON service account key — especially if your GCP organization has disabled service account key creation.

**This route does not work reliably with dbt Cloud.** The "Save" button keeps turning into "Retry" regardless of your WIF configuration (pool, principal, OAuth client, etc.).

The solution is to remove the organization policy that blocks service account key creation:

1. Grant yourself **Service Account Key Admin** and **Organization Policy Administrator** roles at the organization level.

2. Delete the policy that prevents key creation:
```bash
gcloud org-policies delete iam.disableServiceAccountKeyCreation --organization=[your-org-id]
```

Note: Manually disabling legacy and enforced policies via the GCP Console may not work — the CLI command above is what actually removes the restriction.

3. Now you can create a JSON key for your BigQuery service account and proceed with the normal dbt Cloud setup.
