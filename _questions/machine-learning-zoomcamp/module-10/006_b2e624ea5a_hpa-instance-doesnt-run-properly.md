---
id: b2e624ea5a
question: HPA instance doesn’t run properly
sort_order: 6
---

If the HPA instance does not run correctly even after installing the latest version of Metrics Server from the `components.yaml` manifest with:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

And the targets still appear as `<unknown>`, follow these steps:

1. Run the following command to edit the deployment:
   
   ```bash
   kubectl edit deploy -n kube-system metrics-server
   ```
   
2. Search for the line:
   
   ```yaml
   args:
   - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
   ```
   
3. Add the following line in the middle:
   
   ```yaml
   - --kubelet-insecure-tls
   ```
   
   So it looks like this:

   ```yaml
   args:
   - --kubelet-insecure-tls
   - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
   ```

4. Save the changes and run:

   ```bash
   kubectl get hpa
   ```