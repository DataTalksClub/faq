---
id: cee7450404
question: How do I check that my Homework 5 predictions match the reference and container?
sort_order: 6
---

Use Python 3.11.15 and the checked-in `pipeline.bin` from `cohorts/2026/homework/05-deployment/`.

From the repository root, run:

```bash
cd cohorts/2026/homework/05-deployment
uv sync --locked
sha256sum pipeline.bin
```

Compare the SHA-256 output with `model_sha256` in `model_metadata.json`. Don't regenerate `uv.lock`.

For Question 3, load `pipeline.bin` and pass the exact lead dictionary from the homework to `predict_proba` as a one-item list. Read the probability for class 1. The grader allows an absolute error of `0.005`, so submit three decimals. Submit the computed value instead of picking the nearest choice from a list.

For Question 6, send the same request used in Question 4 to the container. Its probability should match Question 4 within `0.005`.

If the values differ, compare `model_sha256` and `feature_defaults_sha256` from `/health` with `model_metadata.json`. When an API request omits features, `predict.py` calls `normalize_record` from `model.py`. It fills missing categorical values with `NA` and numeric values with the training-set medians. Don't replace missing numeric values with zero.

See the [Homework 5 setup and inference instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md), [`predict.py`](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/predict.py), and [`model.py`](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/model.py).
