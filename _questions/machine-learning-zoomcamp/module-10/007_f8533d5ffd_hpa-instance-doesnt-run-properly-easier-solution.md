---
id: f8533d5ffd
question: HPA instance doesn’t run properly (easier solution)
sort_order: 7
---

If the HPA instance does not run correctly even after installing the latest version of Metrics Server from the components.yaml manifest with:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

And the targets still appear as `<unknown>`, run the following command:

```bash
kubectl apply -f https://raw.githubusercontent.com/Peco602/ml-zoomcamp/main/10-kubernetes/kube-config/metrics-server-deployment.yaml
```

This uses a metrics server deployment file already embedding the `--kubelet-insecure-tls` option.