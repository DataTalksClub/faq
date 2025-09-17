---
id: ad15f21a9f
question: TypeError: send_file() unexpected keyword 'max_age' during MLflow UI Launch
section: Module 2: Experiment tracking
course: mlops-zoomcamp
sort_order: 1040
---

Problem: When I ran `$ mlflow ui` on a remote server and try to open it in my local browser I got an exception  and the page with mlflow ui wasn’t loaded.

Solution: You should `pip uninstall flask` on your remote server on conda env and after it install Flask `pip install Flask`. It is because the base conda env has ~flask<1.2, and when you clone it to your new work env, you are stuck with this old version.

Added by Salimov Ilnaz

