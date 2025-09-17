---
course: machine-learning-zoomcamp
id: 554fac782d
question: Your Pipfile.lock (221d14) is out of date (during Docker build)
section: 5. Deploying Machine Learning Models
sort_order: 2120
---

If during running the  docker build command, you get an error like this:

Your Pipfile.lock (221d14) is out of date. Expected: (939fe0).

Usage: pipenv install [OPTIONS] [PACKAGES]...

ERROR:: Aborting deploy

Option 1: Delete the pipfile.lock via rm Pipfile, and then rebuild the lock via  pipenv lock from the terminal before retrying the docker build command.

Option 2:  If it still doesn’t work, remove the pipenv environment, Pipfile and Pipfile.lock, and create a new one before building docker again. Commands to remove pipenv environment and removing pipfiles:

pipenv  --rm

rm Pipfile*

