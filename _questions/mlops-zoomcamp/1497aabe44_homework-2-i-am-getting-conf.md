---
id: 1497aabe44
question: Homework 2 , I am getting conflicts on server ports and cannot establish a connection to the MLflow server, why?
section: General course questions
course: mlops-zoomcamp
sort_order: 160
---

Your port (5000) may be in use by some other process ID, run ‘lsoft -i :5000’ to find out and either kill the process or explicitly route to a different port (than the default) with ‘mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5001’

