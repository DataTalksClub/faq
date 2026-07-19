---
id: c306f20bf3
question: dlt.attach() in the deployment lesson uses the wrong dataset name—how do
  I fix it for the REST API pipeline dashboard?
sort_order: 10
---

The lesson 06 dashboard deploy snippet may show `dlt.attach("agent_traces", destination="playground", dataset_name="agent_logs")`, but that `dataset_name` must match what your deployed REST API pipeline actually writes.

In the reference REST API pipeline (lesson 4, e.g. `code/rest_api_pipeline.py`), the pipeline is created with `dataset_name="traces"` (not `agent_logs`). The snippet likely got copied from the lesson 2 filesystem pipeline, where `agent_logs` is the dataset name.

Fix:
- Open your `rest_api_pipeline.py` and check the `dlt.pipeline(..., dataset_name="...")` call.
- Use that exact dataset name in your dashboard attach, e.g. `dlt.attach("agent_traces", destination="playground", dataset_name="traces")`.

This avoids ambiguous DuckDB catalog/schema resolution and ensures the dashboard connects to the data your pipeline produced.