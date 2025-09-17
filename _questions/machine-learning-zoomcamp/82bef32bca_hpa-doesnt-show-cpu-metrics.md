---
id: 82bef32bca
question: HPA doesn’t show CPU metrics
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3660
---

Problem: CPU metrics Shows Unknown

NAME         REFERENCE           TARGETS         MINPODS   MAXPODS   REPLICAS   AGE

credit-hpa   Deployment/credit   <unknown>/20%   1         3         1          18s

FailedGetResourceMetric       2m15s (x169 over 44m)  horizontal-pod-autoscaler  failed to get cpu utilization: unable to get metrics for resource cpu: unable to fetch metrics from resource metrics API:

Solution:

-> Delete HPA (kubectl delete hpa credit-hpa)

-> kubectl apply -f

-> Create HPA

This should solve the cpu metrics report issue.

Added by Priya V

