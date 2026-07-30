---
id: ba1d5f13e7
question: Why does my SQLite exporter receive no spans, or report "Overriding
  of current TracerProvider is not allowed"?
sort_order: 1
---

OpenTelemetry allows the global tracer provider to be registered only once per
Python process. In a notebook, creating another `TracerProvider` and calling
`trace.set_tracer_provider(provider)` again doesn't replace the first provider.
A tracer returned by `trace.get_tracer(...)` therefore remains connected to the
original exporter, which can leave `traces.db` empty.

Restart the kernel, replace the exporter in the original setup cell, and run the
setup cells once in order.

If you intentionally need an independent provider for manually created spans,
get the tracer directly from it:

```python
tracer = provider.get_tracer("llm-zoomcamp")
```

In a script, initialize the provider and exporter once. Separate
`python script.py` runs start fresh Python processes, so they don't share the
previous global provider.
