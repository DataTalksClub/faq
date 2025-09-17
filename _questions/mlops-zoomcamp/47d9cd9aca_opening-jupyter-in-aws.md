---
course: mlops-zoomcamp
id: 47d9cd9aca
question: Opening Jupyter in AWS
section: 'Module 1: Introduction'
sort_order: 300
---

Faced issue while setting up JUPYTER NOTEBOOK on AWS. I was unable to access it from my desktop. (I am not using visual studio and hence faced problem)

Run

jupyter notebook --generate-config

Edit file /home/ubuntu/.jupyter/jupyter_notebook_config.py to add following line:

NotebookApp.ip = '*'

Added by Atul Gupta ()

