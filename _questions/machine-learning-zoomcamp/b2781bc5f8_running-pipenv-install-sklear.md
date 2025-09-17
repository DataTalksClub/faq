---
course: machine-learning-zoomcamp
id: b2781bc5f8
question: Running “pipenv install sklearn==1.0.2” gives errors. What should I do?
section: 5. Deploying Machine Learning Models
sort_order: 1850
---

When the facilitator was adding sklearn to the virtual environment in the lectures, he used sklearn==0.24.1 and it ran smoothly. But while doing the homework and you are asked to use the 1.0.2 version of sklearn, it gives errors.

The solution is to use the full name of sklearn. That is, run it as “pipenv install scikit-learn==1.0.2” and the error will go away, allowing you to install sklearn for the version in your virtual environment.

Odimegwu David

Homework asks you to install 1.3.1

Pipenv install scikit-learn==1.3.1

Use Pipenv to install Scikit-Learn version 1.3.1

Gopakumar Gopinathan

