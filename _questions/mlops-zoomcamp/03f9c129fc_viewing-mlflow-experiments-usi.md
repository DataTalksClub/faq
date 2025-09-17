---
course: mlops-zoomcamp
id: 03f9c129fc
question: Viewing MLflow Experiments using MLflow CLI
section: 'Module 2: Experiment tracking'
sort_order: 1090
---

Problem: After starting the tracking server, when we try to use the mlflow cli commands as listed , most of them can’t seem to find the experiments that have been run with the tracking server

Solution: We need to set the environment variable MLFLOW_TRACKING_URI to the URI of the sqlite database. This is something like “export MLFLOW_TRACKING_URI=sqlite:///{path to sqlite database}” . After this, we can view the experiments from the command line using commands like “mlflow experiments search”

Even after this commands like “mlflow gc” doesn’t seem to get the tracking uri, and they have to be passed explicitly as an argument every time the command is run.

Ahmed Fahim (afahim03@yahoo.com)

