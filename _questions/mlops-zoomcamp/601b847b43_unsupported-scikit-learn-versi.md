---
id: 601b847b43
question: Unsupported Scikit-Learn version
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1070
---

Getting the following warning when running mlflow.sklearn:

2022/05/28 04:36:36 WARNING mlflow.utils.autologging_utils: You are using an unsupported version of sklearn. If you encounter errors during autologging, try upgrading / downgrading sklearn to a supported version, or try upgrading MLflow. […]

Solution: use 0.24.1 <= scikit-learn <= 1.4.2 (Updated: May 26, 2024)

Reference:

