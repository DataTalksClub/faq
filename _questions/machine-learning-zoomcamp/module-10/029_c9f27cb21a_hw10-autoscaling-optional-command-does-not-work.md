---
id: c9f27cb21a
question: HW10 Autoscaling (optional) command does not work
sort_order: 29
---

The following command encountered issues:

```bash
kubectl autoscale deployment subscription --name subscription-hpa --cpu-percent=20 --min=1 --max=3
```

Error logs indicated certificate validation issues due to the server's certificate lacking a valid Subject Alternative Name (SAN) for the node's IP address.

Suggested Steps:

1. Run the following command to skip TLS verification:
   
   ```bash
   kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
   ```

2. Restart the deployment:
   
   ```bash
   kubectl rollout restart deployment metrics-server -n kube-system
   ```

Note: Avoiding TLS certificate validation is not recommended for production systems, but may suffice for this case.