---
course: mlops-zoomcamp
id: 6b1c62c9cf
question: 'WARNING: mlflow.sklearn: Failed to log training dataset information to
  MLflow Tracking.'
section: 'Module 2: Experiment tracking'
sort_order: 1210
---

Problem: When using MLflow’s autolog function, I get this warning: "WARNING mlflow.sklearn: Failed to log training dataset information to MLflow Tracking. Reason: 'numpy.ndarray' object has no attribute 'toarray'". Why is this happening?

Solution:

You're getting this warning because autolog is attempting to log your dataset. Mlflow expects the dataset to be in a pd.DataFrame format, but if you’re following the course’s code, we’re providing a numpy.ndarray. So, when Mlflow tries to do the execute the toarray method, it fails because the numpy.ndarray is already an array.

Since we're not doing anything (yet) with the datasets in this zoomcamp, I just went ahead and put log_datasets = False as a parameter in the autolog function.

Added by Fustincho

Problem: If you get an error while trying to run the mlflow server on AWS CLI with S3 bucket and POSTGRES database:

Reproducible Command:

mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri postgresql://<DB_USERNAME>:<DB_PASSWORD>@<DB_ENDPOINT>:<DB_PORT>/<DB_NAME> --default-artifact-root s3://<BUCKET_NAME>

Error:

"urllib3 v2.0 only supports OpenSSL 1.1.1+, currently "

ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168

Solution: Upgrade mlflow using

Code: pip3 install --upgrade mlflow

Resolution: It downgrades urllib3 2.0.3 to 1.26.16 which is compatible with mlflow and ssl 1.0.2

Installing collected packages: urllib3

Attempting uninstall: urllib3

Found existing installation: urllib3 2.0.3

Uninstalling urllib3-2.0.3:

Successfully uninstalled urllib3-2.0.3

Successfully installed urllib3-1.26.16

Added by Sarvesh Thakur

