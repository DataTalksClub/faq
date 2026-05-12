---
id: 2d5c32331e
question: 'UserWarning: Trying to unpickle estimator from version X.Y.Z when using version A.B.C'
sort_order: 63
---

The model was pickled with a different sklearn version than your runtime has. The warning sometimes works ("Will it actually be wrong? Maybe!"), sometimes the unpickle outright fails.

Pin the same version in your deployment env:

```bash
pipenv install scikit-learn==1.5.2
# or
uv add scikit-learn==1.5.2
```

If you don't know the version the model was pickled with, retrain it with whichever sklearn you're going to deploy.
