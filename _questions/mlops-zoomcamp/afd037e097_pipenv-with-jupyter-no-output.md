---
course: mlops-zoomcamp
id: afd037e097
question: Pipenv with Jupyter no output
section: 'Module 4: Deployment'
sort_order: 1600
---

Problem: I tried to run starter notebook on pipenv environment but had issues with no output on prints. 
I used scikit-learn==1.2.2 and python==3.10
Tornado version was 6.3.2

Solution: The error you're encountering seems to be a bug related to Tornado, which is a Python web server and networking library. It's used by Jupyter under the hood to handle networking tasks.

Downgrading to tornado==6.1 fixed the issue

