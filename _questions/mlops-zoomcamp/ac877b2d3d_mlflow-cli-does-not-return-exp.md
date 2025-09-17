---
course: mlops-zoomcamp
id: ac877b2d3d
question: Mlflow CLI does not return experiments
section: 'Module 2: Experiment tracking'
sort_order: 1080
---

Problem: CLI commands (mlflow experiments list) do not return experiments

Solution description: need to set environment variable for the Tracking URI:
$ export MLFLOW_TRACKING_URI=http://127.0.0.1:5000

Added and Answered by Dino Vitale

