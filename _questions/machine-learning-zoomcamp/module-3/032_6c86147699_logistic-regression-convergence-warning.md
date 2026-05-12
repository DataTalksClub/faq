---
id: 6c86147699
question: 'ConvergenceWarning: lbfgs failed to converge on LogisticRegression'
sort_order: 32
---

The default `max_iter` in `LogisticRegression` is 100, which often isn't enough. Either:

- Increase `max_iter`:
  ```python
  LogisticRegression(max_iter=1000)
  ```
- Scale your features first (StandardScaler).

To suppress the warning while keeping the model:

```python
import warnings
from sklearn.exceptions import ConvergenceWarning
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=ConvergenceWarning)
    # train model here
```

Older course videos used Python 3.8 / older sklearn where this warning didn't appear; with current Python and sklearn it does.
