---
id: 31a648c28a
question: Protobuf error when installing MLflow
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 980
---

Error: I installed all the libraries from the requirements.txt document in a new environment as follows:

pip install -r requirementes.txt

Then when I run mlflow from my terminal like this:

mlflow

I get this error:

![Image](images/mlops-zoomcamp/image_3cc4ae4e.png)

SOLUTION: You need to downgrade the version of 'protobuf' module to 3.20.x or lower. Initially, it was version=4.21, I installed protobuf==3.20

pip install protobuf==3.20

After which I was able to run mlflow from my terminal.

-Submitted by Aashnna Soni

