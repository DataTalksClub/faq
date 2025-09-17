---
id: b062fc29e5
question: TypeError: __init__() got an unexpected keyword argument 'unbound_message' while importing Flask
section: 10. Kubernetes and TensorFlow Serving
course: machine-learning-zoomcamp
sort_order: 3620
---

Problem Description:

In video 10.3, when I was testing a flask service, I got the above error. I ran docker run .. in one terminal. When in second terminal I run python gateway.py, I get the above error.

Solution: This error has something to do with versions of Flask and Werkzeug. I got the same error, if I just import flask with from flask import Flask.

By running pip freeze > requirements.txt,I found that their versions are Flask==2.2.2 and Werkzeug==2.2.2. This error appears while using an old version of werkzeug (2.2.2) with new version of flask (2.2.2). I solved it by pinning version of Flask into an older version with pipenv install Flask==2.1.3.

Added by Bhaskar Sarma

