---
course: machine-learning-zoomcamp
id: 921879ea38
question: Why are FPR and TPR equal to 0.0, when threshold = 1.0?
section: 4. Evaluation Metrics for Classification
sort_order: 1560
---

For churn/not churn predictions, I need help to interpret the following scenario please, what is happening when:

The threshold is 1.0

FPR is 0.0

And TPR is 0.0

When the threshold is 1.0, the condition for belonging to the positive class (churn class) is g(x)>=1.0 But g(x) is a sigmoid function for a binary classification problem. It has values between 0 and 1. This function  never becomes equal to outermost values, i.e. 0 and 1.

That is why there is no object, for which churn-condition could be satisfied. And that is why there is no any positive  (churn) predicted value (neither true positive, nor false positive), if threshold is equal to 1.0

Alena Kniazeva

