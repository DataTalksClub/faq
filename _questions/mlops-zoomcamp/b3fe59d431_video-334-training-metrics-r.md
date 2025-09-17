---
id: b3fe59d431
question: Video 3.3.4 Training Metrics RMSE chart does not show due to the error: KeyError: ‘rmse_LinearRegression’
section: Module 3: Orchestration
course: mlops-zoomcamp
sort_order: 1510
---

Solution: Check the difference between xgboost and sklearn pipelines. In xgboost pipeline there is a track_experiment callback while in sklearn pipeline is not.

Please add those lines:

You can refer them in my similar commit

Added by Nilesh Arte

