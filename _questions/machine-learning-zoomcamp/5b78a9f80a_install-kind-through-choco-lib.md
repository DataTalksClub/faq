---
id: 5b78a9f80a
question: Install kind through choco library
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3510
---

First you need to launch a powershell terminal with administrator privilege.

For this we need to install choco library first through the following syntax in powershell:

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

Krishna Anand

