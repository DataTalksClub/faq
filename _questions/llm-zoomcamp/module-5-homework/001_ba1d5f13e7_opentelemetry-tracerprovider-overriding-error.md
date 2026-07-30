---
id: ba1d5f13e7
question: How to resolve OpenTelemetry Error "Overriding of current TracerProvider
  is not allowed" in LLM Zoomcamp homework?
sort_order: 1
---

OpenTelemetry allows the global tracer provider to be registered only once per
Python process. In a notebook, re-running the setup cell calls
`trace.set_tracer_provider(...)` again and produces this warning.

Restart the kernel, then run the setup cells once in order. When switching from
`ConsoleSpanExporter` to `SQLiteSpanExporter`, edit the original setup cell
instead of running a second provider setup alongside it.

In a script, keep provider initialization in one place and ensure it executes
only once.
