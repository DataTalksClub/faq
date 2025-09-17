---
id: eb3d73e55e
question: Root Mean Squared Error
section: 3. Machine Learning for Classification
course: machine-learning-zoomcamp
sort_order: 1330
---

To use RMSE without math or numpy, ‘sklearn.metrics’ has a mean_squared_error function with a squared kwarg (defaults to True). Setting squared to False will return the RMSE.

from sklearn.metrics import mean_squared_error

rms = mean_squared_error(y_actual, y_predicted, squared=False)

See details:

Ahmed Okka

