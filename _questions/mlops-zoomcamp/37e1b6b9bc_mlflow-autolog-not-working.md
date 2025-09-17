---
course: mlops-zoomcamp
id: 37e1b6b9bc
question: MLflow Autolog not working
section: 'Module 2: Experiment tracking'
sort_order: 910
---

Make sure `mlflow.autolog()` ( or framework-specific autolog ) written BEFORE `with mlflow.start_run()` not after.

Also make sure that all dependencies for the autologger are installed, including matplotlib. A warning about uninstalled dependencies will be raised.

Mohammed Ayoub Chettouh

