---
id: cee7450404
question: How do I check whether my local model inference matches the Docker container in Homework 5?
sort_order: 6
---

Use the same request and model artifact in both environments, and follow the homework's locked dependencies. For Question 6, the container's prediction should match the reference inference from Question 4 within an absolute tolerance of `0.005`.

If the predictions differ, compare the model checksum returned by `/health` with the checksum in `model_metadata.json`. Also check that both runs use the same preprocessing and locked Python dependencies. A different model artifact or dependency set can change the prediction. Different `uv` versions alone don't show that the model or installed packages differ.

See the [Homework 5 setup and container instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md#container).
