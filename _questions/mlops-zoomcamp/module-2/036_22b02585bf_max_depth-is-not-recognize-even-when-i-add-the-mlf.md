---
id: 22b02585bf
question: Max_depth is not recognize even when I add the mlflow.log_params
sort_order: 36
---

Max_depth is not recognized even when I add the `mlflow.log_params`.

The `mlflow.log_params(params)` should be added to the `hpo.py` script. If you run it, it will append the new model to the previous run that doesn’t contain the parameters. You should either:

- Remove the previous experiment
- Change it