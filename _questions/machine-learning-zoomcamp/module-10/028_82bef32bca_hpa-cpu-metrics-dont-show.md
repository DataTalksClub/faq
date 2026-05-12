---
id: 82bef32bca
question: 'HPA: CPU metrics don''t show'
sort_order: 28
---


CPU metrics show "Unknown"

```
NAME         REFERENCE           TARGETS         MINPODS   MAXPODS   REPLICAS   AGE

credit-hpa   Deployment/credit   <unknown>/20%   1         3         1          18s

FailedGetResourceMetric       2m15s (x169 over 44m)  horizontal-pod-autoscaler  failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API:
```


1. Delete HPA:
   ```bash
   kubectl delete hpa credit-hpa
   ```

2. Apply the metrics server configuration:
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/pythianarora/total-practice/master/sample-kubernetes-code/metrics-server.yaml
   ```

3. Recreate the HPA.

This should solve the CPU metrics report issue.

