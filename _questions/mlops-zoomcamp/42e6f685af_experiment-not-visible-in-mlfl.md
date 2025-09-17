---
course: mlops-zoomcamp
id: 42e6f685af
question: Experiment not visible in MLflow UI
section: 'Module 2: Experiment tracking'
sort_order: 830
---

![Image](images/mlops-zoomcamp/image_c5935be1.png)

![Image](images/mlops-zoomcamp/image_d1cb06e4.png)

![Image](images/mlops-zoomcamp/image_54ddd284.png)

Make sure you launch the mlflow UI from the same directory as the code that is running the experiments (same directory that contains the mlruns directory and the database that stores the experiments).

Or navigate to the correct directory when specifying the tracking_uri.

For example:

If the mlflow.db is in a subdirectory called database, the tracking uri would be ‘sqllite:///database/mlflow.db’

If the mlflow.db is a directory above your current directory: the tracking uri would be

‘sqlite:///../mlflow.db’

Answered by Anna Vasylytsya

Another alternative is to use an absolute path to mlflow.db rather than relative path

And yet another alternative is to launch the UI from the same notebook by executing the following code cell

import subprocess

MLFLOW_TRACKING_URI = "sqlite:///data/mlflow.db"

subprocess.Popen(["mlflow", "ui", "--backend-store-uri", MLFLOW_TRACKING_URI])

And then using the same MLFLOW_TRACKING_URI when initializing mlflow or the client

client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

