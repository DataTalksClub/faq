---
id: 06775a8677
question: 'Kestra: how do I authenticate to Google Cloud with a service account?'
sort_order: 7
---

Never paste the service account JSON directly into a Kestra flow — it ends up in version control if you push the flow to GitHub. Use Kestra secrets or the KV store instead.

## Option 1: KV store (simplest, recommended for the course)

1. Open the Namespaces tab in Kestra and select your namespace (e.g. `zoomcamp`).
2. Go to KV Store → New value.
3. Set the key to `GCP_CREDS` (or whatever name your flow expects), set the type to JSON, and paste the contents of your service account key file.
4. Reference it in your flow's `pluginDefaults`:

```yaml
pluginDefaults:
  - type: io.kestra.plugin.gcp
    values:
      serviceAccount: "{{ kv('GCP_CREDS') }}"
      projectId: "{{ kv('GCP_PROJECT_ID') }}"
```

All GCP plugin tasks (BigQuery, GCS, Dataproc, etc.) will pick up the credentials automatically.

## Option 2: Encoded secret (when you can't use KV store)

1. Base64-encode the service account JSON and store it in `.env_encoded` (which must be `.gitignore`d):

```bash
base64 service-account.json > .env_encoded
```

2. Pass the encoded value to Kestra via Docker Compose `environment` and decode it as a Kestra secret. See [Kestra's Google credentials guide](https://kestra.io/docs/how-to-guides/google-credentials#add-service-account-as-a-secret).

3. Reference in flows with `{{ secret('GCP_SERVICE_ACCOUNT') }}`.

## Notes

- Always add `.env_encoded` (and any local copy of the JSON key) to `.gitignore`. Base64 is encoding, not encryption — anyone who sees the file can decode it.
- To rotate the credential: generate a new key in GCP, re-run the encoding/upload step, and restart Kestra.
- Both methods cover all GCP plugins — once configured in `pluginDefaults`, individual tasks (BigQuery, GCS, etc.) inherit the credentials.
