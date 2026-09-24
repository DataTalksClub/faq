---
id: 2f63569378
question: Why does Agent Relay fail to connect to PostgreSQL in a local kind Kubernetes
  cluster when the DB host is set to `localhost`, and what should I change?
sort_order: 4
---

In Kubernetes, `localhost` inside the Agent Relay pod refers to the Agent Relay container itself, not to the PostgreSQL server. So if you set the PostgreSQL host to `localhost:5432`, Agent Relay will look for PostgreSQL inside its own pod and fail.

Change the configuration to use a Kubernetes `Service` hostname instead of `localhost`. For example, if you create a `Service` for PostgreSQL named `postgres`, Agent Relay should connect to `postgres:5432` (or the matching service DNS name in your manifests).

Example `Service`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  selector:
    app: postgres
  ports:
    - port: 5432
      targetPort: 5432
```

Then in Agent Relay’s DB URL, use the service name:
```text
postgresql://<user>:<password>@postgres:5432/<database>
```

If you’re running locally with `kind` and building the Agent Relay image yourself, make sure the image is available to the cluster:
```bash
docker build -t agent-relay:local .
kind load docker-image agent-relay:local
```

After applying manifests, you can verify things by checking pods/services and reviewing logs:
```bash
kubectl get pods
kubectl get services
kubectl logs deployment/agent-relay
```

This is different from Docker Compose: in Compose, container-to-container access can often use service names directly, while Kubernetes requires using Services (and their DNS) for stable cross-pod connectivity.