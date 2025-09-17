---
course: mlops-zoomcamp
id: dcccce53fc
question: Parameter adding in case of max_depth not recognized
section: 'Module 2: Experiment tracking'
sort_order: 1120
---

Problem: parameter was not recognized during the model registry

Solution: parameters should be added in previous to the model registry. The parameters can be added by mlflow.log_params(params) so that the dictionary can be directly appended to the data.run.params.

Added and Answered by Sam Lim

