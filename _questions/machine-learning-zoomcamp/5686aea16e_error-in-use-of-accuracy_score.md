---
course: machine-learning-zoomcamp
id: 5686aea16e
question: Error in use of accuracy_score from sklearn in jupyter (sometimes)
section: 3. Machine Learning for Classification
sort_order: 1350
---

I got this error multiple times here is the code:

“accuracy_score(y_val, y_pred >= 0.5)”

TypeError: 'numpy.float64' object is not callable

I solve it using

from sklearn import metrics

metrics.accuracy_score(y_train, y_pred>= 0.5)

OMAR Wael

