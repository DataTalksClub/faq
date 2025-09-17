---
id: c9f27cb21a
question: HW10 Autoscaling (optional) command does not work
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3670
---

This command never worked:

kubectl autoscale deployment subscription --name subscription-hpa --cpu-percent=20 --min=1 --max=3

Going through the error logs, it indicated some sort of certificate validation issues because of the server's certificate not having a valid Subject Alternative Name (SAN) for the node's IP address.

chatGPT suggested to run in terminal:

kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'

to skip the TLS verification and

kubectl rollout restart deployment metrics-server -n kube-system

to restart the deployment. then the metrics server started working.

Avoiding TLS certificate validation may not be a good solution for production ready systems, but it would be enough for our case.

Till Meineke, Dec 2024

