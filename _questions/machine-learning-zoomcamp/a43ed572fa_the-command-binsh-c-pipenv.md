---
course: machine-learning-zoomcamp
id: a43ed572fa
question: 'The command ''/bin/sh -c pipenv install --deploy --system &&  rm -rf /root/.cache''
  returned a non-zero code: 1'
section: 5. Deploying Machine Learning Models
sort_order: 1840
---

After using the command “docker build -t churn-prediction .” to build the Docker image, the above error is raised and the image is not created.

In your Dockerfile, change the Python version in the first line the Python version installed in your system:

FROM python:3.7.5-slim

To find your python version, use the command python --version. For example:

python --version

>> Python 3.9.7

Then, change it on your Dockerfile:

FROM python:3.9.7-slim

Added by

