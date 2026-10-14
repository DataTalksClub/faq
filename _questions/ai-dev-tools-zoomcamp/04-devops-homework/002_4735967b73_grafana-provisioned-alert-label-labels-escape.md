---
id: 4735967b73
question: "My provisioned Grafana alert label shows \"{{ .http_route }}\" instead of the route. Why?"
sort_order: 2
---

Grafana's file provisioning replaces environment variables (`$VAR`, `${VAR}`) in most alerting properties, including rule labels and contact point settings. In `route: "{{ $labels.http_route }}"`, `$labels` is treated as an unset variable and replaced with an empty string, so the rule is stored with `{{ .http_route }}`. Rule annotations are not interpolated, which is why the same template works there.

Escape the dollar sign with `$$` in labels, and in any other interpolated property such as a contact point's `subject`:

```yaml
labels:
  severity: critical
  route: "{{ $$labels.http_route }}"
annotations:
  summary: "5xx on {{ $labels.http_route }}"
```

This only applies to provisioning files. Rules created in the UI use a single `$`. To check, open the rule in **Alerting > Alert rules** and look at the stored label.

See [Grafana: template variable interpolation in provisioning](https://grafana.com/docs/grafana/latest/alerting/set-up/provision-alerting-resources/file-provisioning/).
