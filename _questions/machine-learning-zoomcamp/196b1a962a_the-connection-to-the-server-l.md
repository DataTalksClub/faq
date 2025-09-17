---
id: 196b1a962a
question: The connection to the server localhost:8080 was refused - did you specify the right host or port?
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3530
---

I ran into an issue where kubectl wasn't working.

I kept getting the following error:

kubectl get service

The connection to the server localhost:8080 was refused - did you specify the right host or port?

I searched online for a resolution, but everyone kept talking about creating an environment variable and creating some admin.config file in my home directory.

All hogwash.

The solution to my problem was to just start over.

kind delete cluster

rm -rf ~/.kube

kind create cluster

Now when I try the same command again:

kubectl get service

NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE

kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   53s

Added by Martin Uribe

