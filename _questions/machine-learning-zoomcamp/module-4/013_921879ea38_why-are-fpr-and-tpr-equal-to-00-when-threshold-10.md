---
id: 921879ea38
question: Why are FPR and TPR equal to 0.0, when threshold = 1.0?
sort_order: 13
---

For churn/not churn predictions, when the threshold is 1.0:

- **FPR** (False Positive Rate) is 0.0
- **TPR** (True Positive Rate) is 0.0

When the threshold is set to 1.0, the condition for belonging to the positive class (churn class) is `g(x) >= 1.0`. However, `g(x)` is a sigmoid function in a binary classification problem, which produces values between 0 and 1. The function never reaches the outermost values of 0 or 1.

Therefore, no sample will satisfy the condition for the positive class (churn), resulting in no positive (churn) predictions. Consequently, this leads to both the false positive and true positive rates being 0.0 when the threshold is 1.0.