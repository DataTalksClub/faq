---
id: 364a95b2c9
question: "HW4 Q6: My Grafana alert is Firing but the webhook never reaches my responder on localhost:8001. How do I fix it?"
sort_order: 4
---

Grafana runs in a container, so `localhost` in the contact point URL means the Grafana container itself, not your machine.

1. Point the webhook at the host:

   ```yaml
   contactPoints:
     - orgId: 1
       name: incident-responder
       receivers:
         - uid: incident-responder-webhook
           type: webhook
           settings:
             url: http://host.docker.internal:8001/alerts
             httpMethod: POST
   ```

2. On Linux (and Colima or other non-Desktop engines), map that hostname in `docker-compose.yaml`. Docker Desktop on Mac and Windows provides it automatically:

   ```yaml
   grafana:
     extra_hosts:
       - "host.docker.internal:host-gateway"
   ```

3. Bind the responder to all interfaces, not just `127.0.0.1`, for example `uvicorn app:app --host 0.0.0.0 --port 8001`.

4. Test from inside the Grafana container before waiting for a real alert:

   ```bash
   docker compose exec grafana wget -qO- --header='Content-Type: application/json' \
     --post-data='{"alerts":[]}' http://host.docker.internal:8001/alerts
   ```

   Or use **Alerting > Contact points > Test**.

5. If the alert already fired before the webhook worked, Grafana won't resend it until the repeat interval passes. Let the alert return to Normal and trigger the failing request again.

Alternatively, run the responder as a service in the same Compose file and use its service name, for example `http://responder:8001/alerts`.

See [Docker: add host entries](https://docs.docker.com/reference/cli/docker/container/run/#add-host).
