---
id: ba1d5f13e7
question: How to resolve OpenTelemetry Error "Overriding of current TracerProvider
  is not allowed" in LLM Zoomcamp homework?
sort_order: 8
---

This error typically happens when OpenTelemetry’s tracing is initialized more than once in the same kernel/session (e.g., after changing `ConsoleSpanExporter` to `SQLiteSpanExporter` for storing LLM calls in sqlite).

How to fix it:
- Restart the kernel.
- Re-run the homework so that `TraceProvider` is loaded only once and without any earlier initialization errors.

After restarting, you should be able to use the new exporter and avoid the “Overriding of current TracerProvider is not allowed” message.