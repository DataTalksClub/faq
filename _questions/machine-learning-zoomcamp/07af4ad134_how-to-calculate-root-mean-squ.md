---
course: machine-learning-zoomcamp
id: 07af4ad134
question: How to calculate Root Mean Squared Error?
section: 3. Machine Learning for Classification
sort_order: 1310
---

We can use sklearn & numpy packages to calculate Root Mean Squared Error

from sklearn.metrics import mean_squared_error

import numpy as np

Rmse = np.sqrt(mean_squared_error(y_pred, y_val/ytest)

Added by Radikal Lukafiardi

You can also refer to Alexey’s notebook for Week 2:

https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/chapter-02-car-price/02-carprice.ipynb

which includes the following code:

def rmse(y, y_pred):

error = y_pred - y

mse = (error ** 2).mean()

return np.sqrt(mse)

(added by Rileen Sinha)

