---
course: mlops-zoomcamp
id: 22b02585bf
question: Max_depth is not recognize even when I add the mlflow.log_params
section: 'Module 2: Experiment tracking'
sort_order: 1130
---

Problem: Max_depth is not recognize even when I add the mlflow.log_params

Solution: the mlflow.log_params(params) should be added to the hpo.py script, but if you run it it will append the new model to the previous run that doesn’t contain the parameters, you should either remove the previous experiment or change it

Pastor Soto

