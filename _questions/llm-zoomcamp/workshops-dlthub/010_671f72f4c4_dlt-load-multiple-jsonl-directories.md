---
id: 671f72f4c4
question: Can I load multiple JSONL log directories into the same dlt pipeline?
sort_order: 10
---

Yes. Build one filesystem resource for each directory and pass the resources
together to the same pipeline, as the workshop's reference
`filesystem_pipeline.py` does for Claude and Codex logs.

For JSONL files with the same structure:

```python
import dlt
from dlt.sources.filesystem import filesystem, read_jsonl

pipeline = dlt.pipeline(
    pipeline_name="agent_logs",
    destination="duckdb",
    dataset_name="agent_logs",
)

resources = []
for name, directory in {
    "claude": "/home/me/.claude/projects",
    "codex": "/home/me/.codex/sessions",
}.items():
    resource = (
        filesystem(
            bucket_url=f"file://{directory}",
            file_glob="**/*.jsonl",
        )
        | read_jsonl()
    ).with_name(name)
    resources.append(resource)

pipeline.run(
    resources,
    table_name="log_records",
    write_disposition="append",
)
```

Replace the example paths with your directories. `table_name` sends the
resources to the same table, and dlt can add columns as the schema evolves.
For heterogeneous agent logs, reuse the workshop's `raw_reader()` transformer
so each line is preserved consistently before loading.
