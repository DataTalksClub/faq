---
id: 61b908fe84
question: 'BigQuery: "Cannot read and write in different locations" when loading from
  GCS'
sort_order: 8
---

BigQuery cannot load data from a GCS bucket into a dataset in a different region — they must match. If your bucket is in `EU` and your BigQuery dataset is in `US` (or `us-central1` vs `asia-south2`, etc.), you'll see:

```
Cannot read and write in different locations: source: <region-A>, destination: <region-B>
```

## Fix

1. Check the bucket's region in the GCS console (the "Location" field on the bucket details page).
2. Create a BigQuery dataset in the same region. Click the three-dot menu next to your project → "Create dataset" → set "Data location" to match the bucket exactly (e.g. `us-central1`, not just `US`).
3. Load the data into this newly-created dataset.

If you only ever need one region, set up your project resources (bucket and dataset) in the same region from the start.

For dbt-specific region issues (datasets created automatically by `dbt build`, prod vs dev mismatches, CI), see the corresponding dbt + BigQuery region FAQ in module 4.
