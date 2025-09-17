---
id: b2e624ea5a
question: HPA instance doesn’t run properly
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3460
---

In case the HPA instance does not run correctly even after installing the latest version of Metrics Server from the components.yaml manifest with:

>>kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

And the targets still appear as <unknown>

Run >>kubectl edit deploy -n kube-system metrics-server

And search for this line:

args:

- --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname

Add this line in the middle:  - --kubelet-insecure-tls

So that it stays like this:

args:

- --kubelet-insecure-tls

- --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname

Save and run again >>kubectl get hpa

Added by Marilina Orihuela

