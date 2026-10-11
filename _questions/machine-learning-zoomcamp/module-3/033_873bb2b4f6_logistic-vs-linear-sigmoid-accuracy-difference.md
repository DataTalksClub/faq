---
id: 873bb2b4f6
question: Why do LogisticRegression and LinearRegression+sigmoid produce different
  accuracy?
sort_order: 33
---

`LogisticRegression` and `LinearRegression` learn their parameters in fundamentally different ways, so their predicted scores/probabilities (and therefore thresholded predictions/accuracy) can differ.

- `LogisticRegression` is trained to minimize the logistic (log) loss for classification. Its weights are optimized so that the model’s output probabilities match the binary labels.

- `LinearRegression` is trained to minimize mean squared error (MSE) between its linear outputs and the target values. If you then apply a sigmoid to those linear outputs, you only change how the already-learned scores are mapped into the 0–1 range—you do not change the training objective that produced the weights.

- Also, neither model directly optimizes accuracy. `LogisticRegression` optimizes logistic loss, while `LinearRegression` optimizes MSE, so there is no guarantee that the `LogisticRegression` solution will always yield higher accuracy than the “regression + sigmoid” approach.

As a result, different loss functions during training typically lead to different decision boundaries/scores, and after applying a classification threshold you can observe different accuracies.