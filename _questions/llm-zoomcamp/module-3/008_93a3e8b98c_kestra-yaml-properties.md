---
id: 93a3e8b98c
question: Why does a generic AI assistant generate Kestra flow YAML with properties
  that don't exist, and how can I avoid it?
sort_order: 8
---

A general AI (e.g., ChatGPT) isn't grounded in Kestra's plugin schemas for your running version, so it can surface plausible but invalid property names (such as `bucket`/`name`) instead of the real, version-specific property. For example:

**GCS Upload** — invented `bucket`/`name` props vs. the real `to` property:

```yaml
# Incorrect (invented props)
- id: upload_to_gcs
  type: "io.kestra.plugin.gcp.gcs.Upload"
  bucket: "my-bucket"
  name: "path/to/file"

# Correct
- id: upload_to_gcs
  type: "io.kestra.plugin.gcp.gcs.Upload"
  to: "gs://my-bucket/path/to/file"
```

**BigQuery LoadFromGcs** — split `projectId`/`dataset`/`table` vs. the real `destinationTable`:

```yaml
# Incorrect (pseudo-split properties)
- id: load_to_bq
  type: "io.kestra.plugin.gcp.bigquery.LoadFromGcs"
  projectId: "my-project"
  dataset: "my_dataset"
  table: "my_table"

# Correct
- id: load_to_bq
  type: "io.kestra.plugin.gcp.bigquery.LoadFromGcs"
  destinationTable: "my-project.my_dataset.my_table"
```

To avoid this:

- Cross-check generated YAML against the official plugin docs: https://kestra.io/plugins/plugin-gcp
- Use Kestra's built-in AI Copilot, which is grounded in the current plugin schema for your running version.
- Validate and test your YAML in your Kestra environment to ensure it parses and runs as expected.

Note that plugin properties can vary by plugin version; what's correct in one release may be invalid in another. If you share a snippet, we can help verify it against the docs.
