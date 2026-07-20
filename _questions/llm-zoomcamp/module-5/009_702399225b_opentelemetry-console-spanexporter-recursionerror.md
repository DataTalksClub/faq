---
id: 702399225b
question: Why does my execution script freeze or crash with `RecursionError` when
  initializing OpenTelemetry with `ConsoleSpanExporter` in Module 5?
sort_order: 9
---

This can happen in local runs on Python 3.14: `ConsoleSpanExporter` may trigger an infinite evaluation loop when it tries to read raw source lines (via `linecache`) to add metadata to the console output.

Workaround: disable the console text exporter and send spans to storage with a custom exporter.

One option is to implement a `SpanExporter` that writes span fields to a local SQLite database, and initialize your `TracerProvider` with that exporter instead of the console processor.

Example custom exporter:

```python
import sqlite3
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult

class SQLiteSpanExporter(SpanExporter):
    def __init__(self, db_path="traces.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS spans (
                name TEXT, start_time INTEGER, end_time INTEGER,
                input_tokens INTEGER, output_tokens INTEGER, cost REAL
            )
            """
        )
        self.conn.commit()

    def export(self, spans):
        for span in spans:
            attrs = dict(span.attributes or {})
            self.conn.execute(
                "INSERT INTO spans VALUES (?, ?, ?, ?, ?, ?)",
                (
                    span.name,
                    span.start_time,
                    span.end_time,
                    attrs.get("input_tokens", 0),
                    attrs.get("output_tokens", 0),
                    attrs.get("cost", 0.0),
                ),
            )
        self.conn.commit()
        return SpanExportResult.SUCCESS
```

After switching to the SQLite exporter, the freeze/crash should stop because the console-based exporter (the part that triggers the recursion) is no longer used.