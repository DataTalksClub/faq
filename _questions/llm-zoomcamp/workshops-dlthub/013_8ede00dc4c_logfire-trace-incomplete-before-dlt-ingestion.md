---
id: 8ede00dc4c
question: Why does the dlt workshop pipeline load fewer Logfire spans or tokens
  than expected?
sort_order: 13
---

Logfire may not have exported and indexed the complete trace when you run the
dlt pipeline immediately after the agent. The Query API can then return only
part of the trace. As a result, dlt loads fewer rows or nested tables and your
token total is too low.

Flush pending telemetry after the agent finishes:

```python
import logfire

if not logfire.force_flush(timeout_millis=10_000):
    raise RuntimeError("Logfire did not finish exporting the trace")
```

Then run the ingestion pipeline. If the Query API still returns only part of
the trace, wait a few seconds and retry the query.

Don't hard-code an expected span count because the model can make a different
number of search calls on each run. Instead, query all records with the same
`trace_id`. For Question 3, compare the sum of
`gen_ai.usage.input_tokens` on the model-call spans with
`gen_ai.aggregated_usage.input_tokens` on the top-level agent-run span. They
should agree once the complete trace is available.
