---
id: 5020067c2b
question: Standard Deviation Differences in Numpy and Pandas
section: 2. Machine Learning for Regression
course: machine-learning-zoomcamp
sort_order: 870
---

Numpy and Pandas packages use different equations to compute the standard deviation. Numpy uses  population standard deviation, whereas pandas uses sample standard deviation by default.

Numpy

![Image](images/machine-learning-zoomcamp/image_38e67375.png)

Pandas

![Image](images/machine-learning-zoomcamp/image_8ad3d822.png)

pandas default standard deviation is computed using one degree of freedom. You can change degree in of freedom in NumPy to change this to unbiased estimator by using ddof parameter:

import numpy as np

np.std(df.weight, ddof=1)

The result will be similar if we change the dof = 1 in numpy

(Harish Balasundaram)

