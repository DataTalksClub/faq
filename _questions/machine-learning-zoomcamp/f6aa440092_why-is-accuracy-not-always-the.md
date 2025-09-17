---
course: machine-learning-zoomcamp
id: f6aa440092
question: Why is accuracy not always the best metric for evaluating a classification
  model?
section: 4. Evaluation Metrics for Classification
sort_order: 1700
---

Accuracy is the proportion of correct predictions made by the model, but it can be misleading, especially with imbalanced datasets. For example, if 95% of your data belongs to one class, a model that always predicts this majority class will have high accuracy, even though it completely fails to identify the minority class. In such cases, metrics like precision, recall, F1-score, or AUROC might be more appropriate, as they provide a clearer view of model performance on both classes.

David Peterson

