---
id: ff4074063c
question: How do you determine the minimum number of replicas needed to guarantee
  zero-downtime for model updates in production, taking startup latency and readiness
  probes into account?
sort_order: 1
---

To guarantee zero-downtime during model updates in production, determine the minimum number of replicas by considering baseline capacity, update duration, and per-pod latency, and by configuring Kubernetes RollingUpdate with readiness and startup probes. The core idea is to ensure that, during an update, enough pods are ready to serve traffic while new pods are brought up and become ready before old pods are terminated. A practical starting point is to run at least two replicas and enable maxUnavailable: 0 with maxSurge: 1, along with proper readinessProbe and startupProbe settings. If startup latency or traffic bursts require more headroom, scale beyond two—the exact minimum depends on your traffic load, pod readiness time, and update window.

Recommended steps:
1. Define your service's baseline concurrency (requests per second) and target latency.
2. Estimate per-pod capacity (how many requests a single pod can handle while staying within latency SLO).
3. Choose deployment strategy:
   - RollingUpdate with maxUnavailable: 0 to avoid taking pods out of service during the update.
   - maxSurge: 1 (or higher) to temporarily run additional pods during upgrades.
4. Implement readinessProbe to ensure traffic is not routed to a pod until it is ready.
5. Implement startupProbe for slow-start scenarios to avoid premature termination of old pods.
6. Compute minimum replicas as the smallest number R such that, during the upgrade, the number of ready pods stays above your required capacity. In practice:
   - If your baseline requirement is 2 pods and you can upgrade one pod at a time, R_min = 2 with maxSurge: 1.
   - If startup latency is high or you expect bursts, set R_min higher (e.g., 3 or 4) to maintain service during upgrades. 

Example Deployment fragment:
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 2
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    spec:
      containers:
        - name: ml-model
          image: my-registry/ml-model:latest
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
          startupProbe:
            httpGet:
              path: /health
              port: 8080
            failureThreshold: 30
            periodSeconds: 5
```

Additional considerations:
- Canary/blue-green deployments can further reduce risk but add complexity.
- Monitor during upgrades (latency, error rate, CPU/memory) and adjust replicas dynamically.
- Use horizontal pod autoscaling with careful cooldown to maintain capacity while updates occur.