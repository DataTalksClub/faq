---
id: 96e6c5ea38
question: For the midterm, do I need to train multiple models or is one enough?
sort_order: 17
---

The rubric:

- 1 point: one model, no parameter tuning.
- 2 points: multiple models (e.g. linear + tree-based), no extensive tuning.
- 3 points: multiple models AND tuned hyperparameters for them.

You only need to deploy ONE final model — your `train.py` and `predict.py` only handle that one. Comparing the others happens in the notebook.
