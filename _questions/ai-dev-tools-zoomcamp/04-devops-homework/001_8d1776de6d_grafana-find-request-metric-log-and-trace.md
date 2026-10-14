---
id: 8d1776de6d
question: "HW4 Q3: How do I find the request metric, its log, and its trace in Grafana?"
sort_order: 1
---

Use **Explore** (compass icon in Grafana's left menu). Pick a data source at the top, Prometheus for metrics, Loki for logs, or Tempo for traces, and set the time range to cover your request.

**Metric:** in Prometheus, search the metrics browser for part of the name (for example `http_server`) rather than the exact name your app prints. OpenTelemetry names are translated on the way in: dots become underscores, the unit is added as a suffix, and histograms are split into `_bucket`, `_count`, and `_sum`. So `http.server.request.duration` becomes `http_server_request_duration_seconds_count`, and the attribute `http.response.status_code` becomes the label `http_response_status_code`. Query the `_count` series and group by route and status code.

**Log:** in Loki, filter by your service name and search for part of the request URL. Expand the line. If your app adds trace context to logs, you'll see a trace ID.

**Trace:** click the link next to the trace ID if Loki is configured to link to Tempo. Otherwise, paste the ID into a Tempo query or search by service name. New traces can take a few seconds to appear.

If one signal is missing, check that the app exports it and that the Collector pipeline routes it to the right backend.

References: [Grafana Explore](https://grafana.com/docs/grafana/latest/explore/), [OpenTelemetry and Prometheus name translation](https://opentelemetry.io/docs/specs/otel/compatibility/prometheus_and_openmetrics/)
