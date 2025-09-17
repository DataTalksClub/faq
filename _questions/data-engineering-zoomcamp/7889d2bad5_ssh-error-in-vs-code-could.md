---
id: 7889d2bad5
question: SSH error in VS Code - “Could not establish connection to "de-zoomcamp": Permission denied (publickey).”
section: Module 2: Workflow Orchestration
course: data-engineering-zoomcamp
sort_order: 1810
---

If you are using Windows, try copying the .ssh folder from the Linux file path to Windows. In the config file, use

IdentityFile C:\Users\<username>\.ssh\gcp

Instead of IdentityFile ~/.ssh/gcp

Another reason: The private key in its file at the local path C:\Users\<username>\.ssh\gcp needs an extra line in the end:

![Image](images/data-engineering-zoomcamp/image_0f494026.png)

