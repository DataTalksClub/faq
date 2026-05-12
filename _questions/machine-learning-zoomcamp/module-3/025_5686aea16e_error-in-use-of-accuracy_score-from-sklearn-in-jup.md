---
id: 5686aea16e
question: Error in use of accuracy_score from sklearn in Jupyter (sometimes)
sort_order: 25
---

I got this error multiple times; here is the code:

```python
accuracy_score(y_val, y_pred >= 0.5)
```

```
TypeError: 'numpy.float64' object is not callable
```

I solved it using:

```python
from sklearn import metrics

metrics.accuracy_score(y_train, y_pred >= 0.5)
```