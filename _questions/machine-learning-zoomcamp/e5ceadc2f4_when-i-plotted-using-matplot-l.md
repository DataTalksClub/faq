---
course: machine-learning-zoomcamp
id: e5ceadc2f4
question: 'When I plotted using Matplot lib to check if median has a tail, I got the
  error below how can one bypass? FutureWarning: is_categorical_dtype is deprecated
  and will be removed in a future version. Use isinstance(dtype, CategoricalDtype)
  instead'
section: Miscellaneous
sort_order: 4170
---

You can probably resolve this by installing the latest version of Pandas. You can do this conveniently from a Jupyter code cell by writing:

!pip install --upgrade pandas

Alternatively, if for whatever reason you don’t want to change your Pandas version, you can suppress warnings:

import warnings

import pandas as pd

# Suppress FutureWarning messages

warnings.simplefilter(action='ignore', category=FutureWarning)

(added by Kemal Dahha)

