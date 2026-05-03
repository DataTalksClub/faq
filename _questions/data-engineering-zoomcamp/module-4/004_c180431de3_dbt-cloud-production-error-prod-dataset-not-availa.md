---
id: c180431de3
question: 'dbt + BigQuery: "Dataset was not found in location" / region mismatch errors'
sort_order: 4
---

This is the single most common dbt+BigQuery problem in the course. The various "404 Not found: Dataset was not found in location X" errors all come down to the same root cause: a region mismatch between

- the source dataset (e.g. `trips_data_all`),
- the dbt-managed dev/prod dataset (e.g. `dbt_<initial><lastname>` or `prod`), and
- the connection's configured location in dbt Cloud or `profiles.yml`.

BigQuery cannot read and write across regions in a single query, and dbt creates new datasets in whatever location its connection is configured to use. If those don't match your source data's region, you'll see one of:

```
404 Not found: Dataset <project>:<schema> was not found in location <region>
Access Denied: ... or perhaps it does not exist in location <region>
```

## Fix

1. Find the location of your source dataset in the BigQuery console (open the dataset → "Details" → "Data location"). Note the exact region string, e.g. `EU`, `US`, `europe-west6`, `us-central1`.

2. Set dbt's connection location to the same value:
   - dbt Cloud: Account settings → Projects → your project → Connection (BigQuery) → Optional Settings → Location.
   - dbt Core: in `profiles.yml`, under your target, set `location: <region>`.

3. If dbt already created datasets in the wrong region, delete those datasets in BigQuery and re-run `dbt build` so they are recreated in the correct region.

4. For dbt Cloud Production / CI jobs specifically:
   - Deploy → Environments → your environment → Settings → Deployment credentials. Confirm "Dataset" matches a dataset that exists in the right region.
   - When CI is creating a new schema for each PR, the location is inherited from the connection's location setting (step 2). Make sure that's set to your source region, not the default `US`.

5. If you genuinely need cross-region data (e.g. source is in `EU` but you want results in `US`), copy or replicate the source dataset into the target region first using BigQuery's dataset-copy feature. Don't try to query across regions.

## In a dbt model

You can also pin a specific model's location via `config()`:

```sql
{{ config(
    materialized='table',
    location='EU'
) }}
```

But it's cleaner to fix this once at the connection level than to repeat it in every model.

## Common variants

- "prod was not found in location EU" → step 2: set connection location to EU, then step 3.
- "Access Denied: ... or perhaps it does not exist in location US" → same, plus check the service account has access.
- "BigQuery adapter: 404 ... in location europe-west6" → set connection location to `europe-west6` exactly (not `EU`).
- A new dataset appears in `US` after a CI run while everything else is in `EU` → step 2 (the connection's location is wrong) and step 4 (CI inherits it).
