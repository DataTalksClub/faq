---
course: mlops-zoomcamp
id: 376ba649d7
question: 'AttributeError: module ''mlflow'' has no attribute ''set_tracking_url'''
section: 'Module 3: Orchestration'
sort_order: 1490
---

In a mage block, the python statement mlflow.set_tracking_uri() was returning an attribute error. This problem was observed when running mage in one container and mlflow in another. If you encounter this, consider that there may be something else in your project with the name “mlflow”.

Insert a statement before the python statement that produces the attribute error: print(mlflow.__file__) to see what the mlflow module points to. It should return a site-packages location, something like '/usr/local/lib/python3.10/site-packages/mlflow/__init__.py'.

If not, you may have another file or folder called “mlflow” that is confusing the python import statement.

Look at the folder name where the mlflow.db is being created via this command (either in command line or in the dockerfile for the mlflow service):

mlflow server --backend-store-uri sqlite:///home/mlflow/mlflow.db --host", "0.0.0.0 --port 5000

If the folder name for the backend store is mlflow, as above, python may be trying to import that instead of the mlflow package you installed. You will need to change the backend-store folder name to something else, like mlflow_data.

Rename the folder it in your local drive (since it gets mounted in docker-compose.yml);

Change the folder name in the dockerfile for the mlflow service (where you specify the backend-store-uri in the mlflow server command)

Change the folder name in docker-compose.yml (when mounting the folder for the mlflow service), e.g. 
Volumes:
  - "${PWD}/mlflow_data:/home/mlflow_data/"

This should resolve the issue of confusing python with which mlflow to import.

If the import mlflow statement now gives a “module not found” error, check the PYTHONPATH variable in the container by ssh-ing into the running container, as follows:

docker ps   (copy the mage container ID)

docker exec -it <container-ID> /bin/bash

echo $PYTHONPATH

If you do not see the path to the site-packages directory for your python version, you will need to add it to the PYTHONPATH environment variable.

To find out what path you should use, execute this from the running container that you have ssh’d into:

Python

>>> import sys

>>> print(sys.path)

You will hopefully see a path for the site-packages directory for your current python version.

Add this to the PYTHONPATH in the Dockerfile for the Mage service with this line:

ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python3.10/site-packages"

Added by Claudia van Dijk

