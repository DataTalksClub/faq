---
id: d94e5cc566
question: Q6: Logged model artifacts lost when mlflow container is down or removed
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1450
---

By default, the logged model and artifacts are stored in a local folder in the mlflow container but not in /home/src/mlflow, so when the container is restarted (after a compose down or container remove) the artifacts are deleted and you can not see them in mlflow UI.

A simple solution to avoid this issue: You can include a new volume in the docker compose service mlflow to map a folder in the local machine to the folder /mlartifacts in the mlflow container:

- "${PWD}/mlartifacts:/mlartifacts/"

Then, every data logged to the experiment will be available when the mlflow container is recreated.

Added by edumunozsala

