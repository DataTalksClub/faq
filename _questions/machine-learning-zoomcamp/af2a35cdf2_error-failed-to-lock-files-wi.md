---
id: af2a35cdf2
question: Error: Failed to lock files with Pipfile.lock
section: 5. Deploying Machine Learning Models
course: machine-learning-zoomcamp
sort_order: 1860
---

When adding libraries to the virtual environment in the lesson 5.5, the trainer used the command pipenv install numpy scikit-learn==0.24.2 flask; however, some people using Python 3.11 or later, may encounter an error, failing to lock files correctly with Pipfile.lock. You may need to install `scikit-learn==1.4.2` as the error you got when running the application is a bit different from the one of the trainer. This should solve the problem.

If you are still having problems, try the following:

● Delete the Pipfile.lock via rm Pipfile; then rebuild the lock via pipenv lock from the terminal.

● If it still doesn't work, delete the pipenv environment, Pipfile and Pipfile.lock, and create a new one. The commands to delete the pipenv environment and pip files are:

`pipenv --rm`

`rm Pipfile*`

Maximilien Eyengue

