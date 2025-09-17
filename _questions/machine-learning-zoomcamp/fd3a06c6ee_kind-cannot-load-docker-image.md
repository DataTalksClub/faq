---
course: machine-learning-zoomcamp
id: fd3a06c6ee
question: Kind cannot load docker image
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3570
---

Problem: Failing to load docker-image to cluster (when you’ved named a cluster)

kind load docker-image zoomcamp-10-model:xception-v4-001

ERROR: no nodes found for cluster "kind"

Solution: Specify cluster name with -n

kind -n clothing-model load docker-image zoomcamp-10-model:xception-v4-001

Andrew Katoch

