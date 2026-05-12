---
id: 5b755bf0f5
question: How do I authenticate dbt with BigQuery when service account key creation
  is disabled and switch to OAuth?
sort_order: 67
---

When running dbt debug with BigQuery, authentication issues can occur if your dbt profile uses method: service-account but Google Cloud enforces iam.disableServiceAccountKeyCreation. In that case, use Google Application Default Credentials / OAuth instead.

Update profiles.yml from:

```
method: service-account
keyfile: "{{ env_var('GOOGLE_APPLICATION_CREDENTIALS') }}"
```

to:

```
method: oauth
```

Example BigQuery profile:

```
default:
  target: dev
  outputs:
    dev:
      type: bigquery
      method: oauth
      project: "{{ env_var('GCP_PROJECT_ID') }}"
      dataset: "{{ env_var('BIGQUERY_DATASET_GOLD') }}"
      threads: 4
      location: "{{ env_var('GCP_REGION', 'europe-west2') }}"
      priority: interactive
```

Then authenticate locally:

```
gcloud auth login
gcloud auth application-default login

gcloud config set project <your-project-id>

gcloud auth application-default set-quota-project <your-project-id>
```

Finally test:

```
dbt debug
```