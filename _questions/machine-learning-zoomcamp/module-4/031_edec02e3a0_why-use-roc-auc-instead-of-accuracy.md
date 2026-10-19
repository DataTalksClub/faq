---
id: edec02e3a0
question: Why use ROC AUC instead of accuracy?
sort_order: 31
---

Accuracy depends on a chosen decision threshold (e.g., classify as positive when the predicted probability ≥ 0.5). If you change that threshold, accuracy changes too.

ROC AUC instead measures how well your model ranks positives above negatives across *all* possible thresholds. It’s threshold-independent.

Accuracy can also be misleading with imbalanced classes. For instance:
- If 58% of examples are positive, a dumb model that predicts “positive” for everyone gets ~58% accuracy without learning anything.
- If only 1% are positive, predicting “negative” for everyone yields ~99% accuracy while finding none of the positives.
ROC AUC isn’t fooled by this: a constant predictor scores around 0.5 (random ranking).

A useful interpretation: AUC is the probability that a randomly chosen positive example receives a higher score than a randomly chosen negative example.

So if your goal is to evaluate the model’s ability to separate classes by ranking (not a specific threshold), ROC AUC is usually a better choice than accuracy.