---
id: f385403427
question: Standard login in Grafana does not work
section: Module 5: Monitoring
course: mlops-zoomcamp
sort_order: 2000
---

When you try to login in Grafana with standard requisites (admin/admin) it throw up an error.

After run grafana-cli admin reset-admin-password admin in Grafana container the problem will be fixed

Added by Artem Glazkov

Command above is deprecated:

Deprecation warning: The standalone 'grafana-cli' program is deprecated and will be removed in the future. Please update all uses of 'grafana-cli' to 'grafana cli'

To enter the docker container with grafana, find the Container ID by running:

docker ps

Then use the Container ID from grafana and prepend it to the command above like this:

lpep_pickup_datetime<container_ID> grafana cli admin reset-admin-password admin

Added by Svetlana Ulianova

