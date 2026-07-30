---
id: 702399225b
question: Why does my execution script freeze or crash with `RecursionError` when
  initializing OpenTelemetry with `ConsoleSpanExporter` in Module 5?
sort_order: 9
---

Upgrade OpenTelemetry first. Older releases did not support Python 3.14, while
current releases do:

```bash
uv add --upgrade opentelemetry-api opentelemetry-sdk
```

Restart the Python process or notebook kernel after upgrading, then run the
`ConsoleSpanExporter` example again. You can confirm which versions the project
uses with:

```bash
uv run python -c "import importlib.metadata as m; print(m.version('opentelemetry-api'), m.version('opentelemetry-sdk'))"
```

If upgrading is not possible, use Python 3.13 for the homework.

Do not replace the console exporter with an incomplete custom exporter merely
to hide the error. When you reach the SQLite question, use the complete
`SQLiteSpanExporter` from the homework, including its `shutdown()` and
`force_flush()` methods.
