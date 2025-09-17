---
id: ac12e26845
question: Metrics not visible in mlflow UI
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 840
---

I encountered the following issue: I was able to run experiments and the different model parameters were visible. However, the metrics, including the “handmade” metric rmse in the training script, were not visible (empty field).

I solved my problem by making sure to specify the “key” and “value” explicitly when using mlflow.log_metric:

mlflow.log_metric(key="rmse",value=rmse)

Added by Mélanie Fouesnard

