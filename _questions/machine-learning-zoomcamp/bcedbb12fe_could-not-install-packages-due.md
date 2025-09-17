---
course: machine-learning-zoomcamp
id: bcedbb12fe
question: 'Could not install packages due to an OSError: [WinError 5] Access is denied'
section: 10. Kubernetes and TensorFlow Serving
sort_order: 3480
---

When I run pip install grpcio==1.42.0 tensorflow-serving-api==2.7.0 to install the libraries in windows machine,  I was getting the below error :

ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\Asia\\anaconda3\\Lib\\site-packages\\google\\protobuf\\internal\\_api_implementation.cp39-win_amd64.pyd'

Consider using the `--user` option or check the permissions.

![Image](images/machine-learning-zoomcamp/image_6e1c348d.png)

Solution description :

I was able to install the libraries using below command:

pip --user install grpcio==1.42.0 tensorflow-serving-api==2.7.0

Asia Saeed

I'm trying to deploy my machine learning model using Kubernetes, but I'm getting an error stating that my Pods are not starting. What could be the problem?

Solution:
This issue can be caused by several factors:

Resource Allocation: Ensure that your Pods have enough CPU and memory resources allocated. If resources are too low, the Kubernetes scheduler might fail to schedule your Pods.

Image Issues: Verify that the Docker image specified for your Pod is correctly built and accessible. If the image cannot be pulled from the repository, the Pod won’t start.

Added by Abdiaziz Qaladid

