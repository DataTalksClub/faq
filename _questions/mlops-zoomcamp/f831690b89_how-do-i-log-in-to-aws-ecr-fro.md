---
course: mlops-zoomcamp
id: f831690b89
question: How do I log in to AWS ECR from the terminal using Docker?
section: 'Module 5: Monitoring'
sort_order: 1900
---

Before (deprecated command):

$(aws ecr get-login --no-include-email)

Now (updated and secure command):

aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin <ACCOUNTID>.dkr.ecr.<REGION>.amazonaws.com

Note: Make sure you specify the correct AWS region where your ECR repository is located (e.g., us-west-1).

If the region is incorrect or not set properly, the login will fail with a 400 Bad Request error — which doesn’t clearly indicate the region is the issue

Added by Maxkaizo (José L Martínez)

Tip: Use a Python Block in Mage to Interact with Your Dockerized ML Model

The most effective way to integrate your machine learning model into a Mage pipeline is to have your Docker container serve the model via an API (like FastAPI or Flask). Then, a custom Python block within your Mage pipeline can easily call this API to get predictions.

Here’s the concise workflow:

1. In Your Docker Container:

Create an API for your model: Use a framework like FastAPI to wrap your model's prediction logic in an API endpoint. For example, create a /predict endpoint that accepts input data and returns the model's output.

Build and run the Docker container: Ensure the container is running and the API is accessible. For local development, you can use docker-compose to run both your model's container and the Mage container, connecting them on the same Docker network for easy communication.

2. In Your Mage Pipeline:

Create a custom Python block: Add a new "transformer" or "data loader" block to your pipeline.

Call the model's API: Inside this block, use a Python library like requests to send the data you want to get predictions for to your model's API endpoint.

Process the results: The block will receive the predictions back from the API. You can then continue your Mage pipeline, using the model's output for further transformations or exporting it to a database or other destination.

