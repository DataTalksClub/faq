---
course: data-engineering-zoomcamp
id: df4171cea7
question: 'Fix: Add extra_hosts for taskRunner in the dbt-build'
section: 'Module 2: Workflow Orchestration'
sort_order: 1950
---

Adds the extraHosts configuration to the taskRunner in the dbt-build task to resolve the issue with host.docker.internal not being recognized on Linux.

taskRunner:

type: io.kestra.plugin.scripts.runner.docker.Docker

extraHosts:

- "host.docker.internal:host-gateway"

