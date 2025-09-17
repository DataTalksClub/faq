---
course: data-engineering-zoomcamp
id: 1ba58ae0e0
question: GCP VM - Error while saving the file in VM via VS Code
section: 'Module 1: Docker and Terraform'
sort_order: 1560
---

Failed to save '<file>': Unable to write file 'vscode-remote://ssh-remote+de-zoomcamp/home/<user>/data_engineering_course/week_2/airflow/dags/<file>' (NoPermissions (FileSystemError): Error: EACCES: permission denied, open '/home/<user>/data_engineering_course/week_2/airflow/dags/<file>')

You need to change the owner of the files you are trying to edit via VS Code. You can run the following command to change the ownership.

ssh

sudo chown -R <user> <path to your directory>

