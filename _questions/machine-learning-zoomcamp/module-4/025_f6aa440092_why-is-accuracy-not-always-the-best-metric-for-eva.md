---
id: f6aa440092
question: Why is accuracy not always the best metric for evaluating a classification
  model?
sort_order: 25
---

Accuracy is the proportion of correct predictions made by the model, but it can be misleading, especially with imbalanced datasets. For example, if 95% of your data belongs to one class, a model that always predicts this majority class will have high accuracy, even though it completely fails to identify the minority class. In such cases, metrics like precision, recall, F1-score, or AUROC might be more appropriate, as they provide a clearer view of model performance on both classes.

Accuracy also depends on the decision threshold (for example, positive when the predicted probability is at least 0.5). ROC AUC is threshold-independent: it measures how well the model ranks positives above negatives across all thresholds. It equals the probability that a randomly chosen positive example gets a higher score than a randomly chosen negative one, and a constant predictor scores 0.5 regardless of class balance.
