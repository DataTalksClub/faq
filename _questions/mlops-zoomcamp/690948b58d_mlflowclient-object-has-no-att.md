---
id: 690948b58d
question: MlflowClient object has no attribute 'list_experiments'
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 900
---

and then removed in the later version

You should use # Register the best model model_uri = f"runs:/{best_run.info.run_id}/model" mlflow.register_model(model_uri=model_uri, name="RandomForestBestModel") instead

Added by Alex Litvinov

