---
id: 8a8f00802a
question: Python_version and Python_full_version error after running pipenv install:
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2110
---

If you install packages via pipenv install, and get an error that ends like this:

pipenv.vendor.plette.models.base.ValidationError: {'python_version': '3.9', 'python_full_version': '3.9.13'}

python_full_version: 'python_version' must not be present with 'python_full_version'

python_version: 'python_full_version' must not be present with 'python_version'

Do this:

open Pipfile in nano editor, and remove either the python_version or python_full_version line, press CTRL+X, type Y and click Enter to save changed

Type pipenv lock to create the Pipfile.lock.

Done. Continue what you were doing

