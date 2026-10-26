---
id: 5e0476b3c5
question: Why should the output of a machine learning model be identical whether running
  locally or in a Docker container?
sort_order: 78
---

In the Docker deployment, the prediction should match what you get locally because the container must run the same trained model and the same preprocessing pipeline on the same input data.

Practically, that means:
- Use the exact same model artifacts inside the container as you used for the local inference (the assignment may provide/verify which model is loaded).
- Ensure the preprocessing steps are the same (the container code should load/run the same feature preparation and input handling as your local code).
- Compare the container’s inference against the expected inference from the assignment’s Question 4, typically with a small numeric tolerance (e.g., absolute tolerance of `0.005`).

For the deployed service verification, the `/health` route is used to provide identifying information (e.g., the SHA-256 hash) for the model being used, so you can confirm the container is using the intended model.