---
id: f8533d5ffd
question: HPA instance doesn’t run properly (easier solution)
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3470
---

In case the HPA instance does not run correctly even after installing the latest version of Metrics Server from the components.yaml manifest with:

>>kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

And the targets still appear as <unknown>

Run the following command:

kubectl apply -f https://raw.githubusercontent.com/Peco602/ml-zoomcamp/main/10-kubernetes/kube-config/metrics-server-deployment.yaml

Which uses a metrics server deployment file already embedding the - --kubelet-insecure-tls option.

Added by Giovanni Pecoraro

