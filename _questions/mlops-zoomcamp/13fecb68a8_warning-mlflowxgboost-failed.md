---
id: 13fecb68a8
question: WARNING mlflow.xgboost: Failed to infer model signature: could not sample data to infer model signature: please ensure that autologging is enabled before constructing the dataset.
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1160
---

Please make sure you following the order below nd enabling the autologging before constructing the dataset. If you still have this issue check that your data is in format compatible with XGBoost.

# Enable MLflow autologging for XGBoost

mlflow.xgboost.autolog()

# Construct your dataset

X_train, y_train = ...

# Train your XGBoost model

model = xgb.XGBRegressor(...)

model.fit(X_train, y_train)

Added by Olga Rudakova

