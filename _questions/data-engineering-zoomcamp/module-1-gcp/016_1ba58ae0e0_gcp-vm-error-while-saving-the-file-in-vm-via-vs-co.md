---
id: 1ba58ae0e0
question: 'GCP VM: Error while saving the file in VM via VS Code'
sort_order: 16
---



```plaintext
Failed to save '<file>': Unable to write file 'vscode-remote://ssh-remote+de-zoomcamp/home/<user>/data_engineering_course/week_2/airflow/dags/<file>' (NoPermissions (FileSystemError): Error: EACCES: permission denied, open '/home/<user>/data_engineering_course/week_2/airflow/dags/<file>')
```

To resolve this issue, you need to change the owner of the files you are trying to edit via VS Code. Follow these steps:

1. Connect to your VM using SSH.

2. Run the following command to change the ownership:

   ```bash
   sudo chown -R <user> <path to your directory>
   ```