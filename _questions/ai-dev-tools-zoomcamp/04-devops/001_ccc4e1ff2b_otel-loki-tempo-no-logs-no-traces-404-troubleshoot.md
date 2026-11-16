---
id: ccc4e1ff2b
question: Grafana Explore shows "No logs volume available" for my service and Tempo
  TraceQL returns 404—what’s missing with OTEL_ENABLED and the OTEL collector?
sort_order: 1
---

If Grafana/Loki shows no logs and Tempo TraceQL returns 404s for traces, it’s commonly two separate miswirings happening at once:

1) Loki has no logs because your app isn’t actually exporting OTLP logs
- Check your logging setup in the backend (for example `backend/app/infra/telemetry/logging_conf.py`). If it only re-exports symbols (e.g. `from .logging import *`) and you never wire the OTLP log exporter/processor, then Loki won’t receive anything.
- Also verify `OTEL_ENABLED` was `true` when the container started; if it was `false`, the backend may never create the `LoggerProvider` + OTLP log exporter.

What to fix (high-level): ensure the backend creates an `opentelemetry.sdk._logs.LoggerProvider` with a `BatchLogRecordProcessor(OTLPLogExporter(...))` and that a handler is attached to your loggers used by the backend (e.g. `clinicops` and `uvicorn.access`). After enabling and restarting, you should see logs appear in Loki (e.g. in Grafana Explore with the right time range).

2) Tempo 404s because the OTEL collector is sending OTLP to the wrong Tempo port
- Tempo’s OTLP gRPC receiver runs on `4317`.
- Tempo’s HTTP API is on `3200`.
- If the OTEL collector exporter is configured to `tempo:3200` for OTLP, the collector will effectively talk “OTLP/gRPC to an HTTP port”, leading to transport errors (often `http2: frame too large`) and no traces will arrive—so TraceQL queries won’t find them (hence 404).

What to fix: update the OTEL collector’s Tempo OTLP exporter endpoint to `tempo:4317` (OTLP gRPC), and keep Tempo’s `server.http_listen_port` (for its HTTP API) as `3200`. Recreate the relevant containers so the collector picks up the corrected config.

Self-checks after the fix
- Look at `docker compose logs otel-collector --tail=10` and confirm there are no repeated `frame too large` errors.
- Optionally `curl http://localhost:3200/status` to confirm Tempo HTTP is alive.
- In Grafana, run a Tempo search again; you should start seeing traces for your service, and the same `trace_id` should be present in Loki log entries if your logs include trace context.