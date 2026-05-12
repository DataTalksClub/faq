---
id: bd885d3d4d
question: How can I integrate my Dockerized ML model into a Mage pipeline?
sort_order: 27
---

The most effective approach is to have your Docker container serve the model via an HTTP API (FastAPI or Flask), then call that API from a custom Python block in Mage.

In your Docker container:

- Wrap your model's prediction logic in an API. With FastAPI, create a `/predict` endpoint that accepts input data and returns the model's output.
- Build and run the container. For local development, run both your model's container and the Mage container with `docker-compose` on the same Docker network so they can reach each other by service name.

In your Mage pipeline:

- Add a custom Python block (a transformer or data loader).
- Inside the block, use `requests` to send your input data to the model's `/predict` endpoint.
- Process the returned predictions and pass them downstream — to a database, another transformer, or an exporter.
