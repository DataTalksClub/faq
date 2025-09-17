---
id: f346d2cc80
question: Q: I get TypeError: got an unexpected keyword argument 'squared' when using mean_squared_error(..., squared=False). Why?
section: Module 1: Introduction
course: mlops-zoomcamp
sort_order: 750
---

A: While calculating the RMSE, I initially used mean_squared_error(..., squared=False), but it failed with a TypeError. It turns out that the squared parameter was only added in scikit-learn 0.22, and in earlier versions it's not recognized. For older versions, RMSE can be computed manually using np.sqrt(mean_squared_error(...)). Alternatively, from version 1.0 onward, there's a dedicated function: root_mean_squared_error(...), which is more explicit and convenient.

from sklearn.metrics import root_mean_squared_error as rmse

rmse = root_mean_squared_error(y_train, y_pred)

print('RMSE:', rmse)

Added by José Luis Martínez (Maxkaizo)

