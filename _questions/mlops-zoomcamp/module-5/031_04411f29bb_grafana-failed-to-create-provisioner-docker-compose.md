---
id: 04411f29bb
question: "Grafana fails with 'Failed to create provisioner' when running `docker-compose
  up --build`"
sort_order: 31
---

If you see this error from Grafana on startup:

```
✗ Failed to create provisioner: Failed to read dashboards config: could not parse provisioning config file: dashboards.yaml error: read /etc/grafana/provisioning/dashboards/dashboards.yaml: is a directory
```

The Grafana `volumes` in your `docker-compose.yml` are mounting a YAML file path, but Grafana sees a directory at that path. Change file references to directory references in the Grafana `volumes` section.

Instead of:

```
/etc/grafana/provisioning/dashboards/dashboards.yaml
```

use:

```
/etc/grafana/provisioning/dashboards/dashboards
```

Apply the same change to all file paths in the Grafana `volumes` block.
