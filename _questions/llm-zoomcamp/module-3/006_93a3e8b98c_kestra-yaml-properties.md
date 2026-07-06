---
id: 93a3e8b98c
question: Why does a generic AI assistant generate Kestra flow YAML with properties
  that don't exist, and how can I avoid it?
sort_order: 6
---

Why generic AI assistants can produce invalid Kestra YAML

Cause: A general AI (e.g., ChatGPT) isn’t grounded in Kestra’s plugin schemas for your running version. It may surface plausible but invalid property names (such as bucket/name) instead of the real, version-specific destination property.

Examples (GCS Upload and BigQuery LoadFromGcs)

- Incorrect (invented props)
```yaml
- id: upload_to_gcs
  type: "io.kestra.plugin.gcp.gcs.Upload"
  bucket: "my-bucket"
  name: "path/to/file"
```

- Correct (real props for GCS Upload)
```yaml
- id: upload_to_gcs
  type: "io.kestra.plugin.gcp.gcs.Upload"
  to: "gs://my-bucket/path/to/file"
```

- Incorrect (pseudo-split properties for BigQuery LoadFromGcs)
```yaml
- id: load_to_bq
  type: "io.kestra.plugin.gcp.bigquery.LoadFromGcs"
  projectId: "my-project"
  dataset: "my_dataset"
  table: "my_table"
```

- Correct (real property for BigQuery LoadFromGcs)
```yaml
- id: load_to_bq
  type: "io.kestra.plugin.gcp.bigquery.LoadFromGcs"
  destinationTable: "my-project.my_dataset.my_table"
```

How to avoid this in practice

- Always cross-check generated YAML against the official plugin docs: https://kestra.io/plugins/plugin-gcp
- Use Kestra’s built-in AI Copilot, which is grounded in the current plugin schema for your running version
- Validate and test your YAML in your Kestra environment to ensure it parses and runs as expected

Notes

- Plugin properties can vary by plugin version; what’s correct in one release may be invalid in another. If you share a snippet, we can help verify it against the docs.