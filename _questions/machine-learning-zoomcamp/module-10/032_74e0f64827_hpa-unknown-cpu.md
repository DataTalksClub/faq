---
id: 74e0f64827
question: 'HPA shows cpu: <unknown>/20% and never scales (kind cluster)'
sort_order: 32
---

The metrics-server in `kind` clusters doesn't trust kubelet's TLS cert by default. Patch it to skip TLS verification:

```bash
kubectl patch deployment metrics-server -n kube-system --type='json' \
    -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
kubectl rollout restart deployment metrics-server -n kube-system
```

After this, `kubectl get hpa <name> --watch` should start showing real CPU percentages and scale up under load. Don't use `--kubelet-insecure-tls` in production.
