---
id: 671f72f4c4
question: Can I load multiple JSONL log directories into the same dlt pipeline?
sort_order: 10
---

Yes. A single `dlt` pipeline can ingest data from multiple JSONL directories as long as your `source` function iterates over all files (and yields records).

For example, you can walk a directory tree and yield records from each `*.jsonl` file:

```python
from pathlib import Path

def source():
    for path in Path("logs").rglob("*.jsonl"):
        yield from read_jsonl(path)
```

If the JSON files share the same structure, `dlt` will append them into the same table. If schemas differ, `dlt` can evolve the table by adding new columns when needed. This is handy for aggregating logs from multiple projects or different coding agent sessions into one dataset.