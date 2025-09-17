---
course: mlops-zoomcamp
id: aed2f8ddb9
question: Unable to create new Experiment
section: 'Module 2: Experiment tracking'
sort_order: 850
---

Following the instructions as per the video as below did not work though the jupyter notebook says it is successfully created.

![Image](images/mlops-zoomcamp/image_d1cb06e4.png)

Set the URI to the listener directly. It worked for me. This could be because the video was made with a lower version of the “mlflow” package and we are working on the latest version. The documentation of the latest  “mlflow” package is asking to set as below

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

(optional) Arun Gansi

