---
id: 196b1a962a
question: The connection to the server localhost:8080 was refused - did you specify
  the right host or port?
sort_order: 14
---

I encountered an issue where `kubectl` wasn't working, and I received the following error when trying to execute a command:

```bash
kubectl get service

The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

Here is the solution that worked for me:

1. Delete the existing cluster:
   
   ```bash
   kind delete cluster
   ```

2. Remove the Kubernetes configuration directory:

   ```bash
   rm -rf ~/.kube
   ```

3. Create a new cluster:

   ```bash
   kind create cluster
   ```

After performing these steps, the command worked successfully:

```bash
kubectl get service

NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   53s
```