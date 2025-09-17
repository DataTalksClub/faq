---
course: mlops-zoomcamp
id: 8231e2605d
question: 'MLflow container error: Can''t locate revision identified by …'
section: 'Module 3: Orchestration'
sort_order: 1420
---

This means your MLflow container tries to access a db file which was a backend for a different MLflow version than the one you have in the container. Most likely, the MLflow version in the container does not match the MLflow version of the MLflow server you ran in module 2.

The easiest solution is to check which version you worked with before, and change the docker image accordingly.

You can check your version by opening a terminal on your host, conda activate into the env you worked in, and run:

mlflow --version

Now edit the mlflow.dockerfile line to your version:

RUN pip install mlflow==2.??.??

Save the file and rebuild the docker service by running:

docker-compose build

Now you can start up the containers again and your MLflow container should be able to successfully read your mounted DB file.

