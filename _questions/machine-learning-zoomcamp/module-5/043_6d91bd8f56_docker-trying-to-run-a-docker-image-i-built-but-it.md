---
id: 6d91bd8f56
question: 'Docker: Trying to run a docker image I built but it says it’s unable to
  start the container process'
sort_order: 43
---

Ensure that you used `pipenv` to install the necessary modules including `gunicorn`. Follow these steps:

1. Use `pipenv shell` to enter the virtual environment.
2. Build and run your Docker image.

Make sure all dependencies are correctly specified in your Pipfile.