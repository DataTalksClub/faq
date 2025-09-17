---
course: mlops-zoomcamp
id: 1b858ee8bb
question: No module named 'pip._vendor.six'
section: 'Module 4: Deployment'
sort_order: 1580
---

During scikit-learn installation via the command:

pipenv install scikit-learn==1.0.2

The following error is raised:

ModuleNotFoundError: No module named 'pip._vendor.six'

Then, one should:

sudo apt install python-six

pipenv --rm

pipenv install scikit-learn==1.0.2

Added by Giovanni Pecoraro

