---
id: 8a8e4f34a7
question: Image size of 460x93139 pixels is too large. It must be less than 2^16 in each direction.
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 890
---

This is caused by ```mlflow.xgboost.autolog()``` when version 1.6.1 of xgboost
Downgrade to 1.6.0

```pip install xgboost==1.6.0``` or update requirements file with xgboost==1.6.0 instead of xgboost

Added by Nakul Bajaj

