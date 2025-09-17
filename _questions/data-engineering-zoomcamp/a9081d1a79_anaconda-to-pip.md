---
id: a9081d1a79
question: Anaconda to PIP
section: Module 1: Docker and Terraform
course: data-engineering-zoomcamp
sort_order: 1780
---

To get a pip-friendly requirements.txt file file from Anaconda use

conda install pip then `pip list –format=freeze > requirements.txt`.

`conda list -d > requirements.txt` will not work and `pip freeze > requirements.txt` may give odd pathing.

