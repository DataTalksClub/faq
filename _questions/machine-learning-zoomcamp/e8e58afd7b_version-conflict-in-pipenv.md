---
id: e8e58afd7b
question: Version-conflict in pipenv
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 2100
---

Problem description:

In video 5.5 when I do pipenv shell and then pipenv run gunicorn --bind 0.0.0.0:9696 predict:app, I get the following warning:

UserWarning: Trying to unpickle estimator DictVectorizer from version 1.1.1 when using version 0.24.2. This might lead to breaking code or invalid results. Use at your own risk.

Solution description:

When you create a virtual env, you should use the same version of Scikit-Learn that you used for training the model on this case it's 1.1.1. There is version conflicts so we need to make sure our model and dv files are created from the version we are using for the project.

Bhaskar Sarma

