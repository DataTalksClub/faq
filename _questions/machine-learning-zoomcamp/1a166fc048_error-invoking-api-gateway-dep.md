---
course: machine-learning-zoomcamp
id: 1a166fc048
question: Error invoking API Gateway deploy API locally
section: 9. Serverless Deep Learning
sort_order: 3220
---

Problem: Trying to test API gateway in , running: $ python test.py

With error message:

{'message': 'Missing Authentication Token'}

Solution:

Need to get the deployed API URL for the specific path you are invoking. Example:

https://<random string>.execute-api.us-east-2.amazonaws.com/test/predict

Added by Andrew Katoch

