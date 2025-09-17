---
course: machine-learning-zoomcamp
id: c30519737d
question: Understanding RMSE and how to calculate RMSE score
section: 2. Machine Learning for Regression
sort_order: 900
---

The Root Mean Squared Error (RMSE) is one of the primary metrics to evaluate the performance of a regression model. It calculates the average deviation between the model's predicted values and the actual observed values, offering insight into the model's ability to accurately forecast the target variable. To calculate RMSE score:

Libraries needed

import numpy as np

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(actual_values, predicted_values)

rmse = np.sqrt(mse)

print("Root Mean Squared Error (RMSE):", rmse)

(Aminat Abolade)

