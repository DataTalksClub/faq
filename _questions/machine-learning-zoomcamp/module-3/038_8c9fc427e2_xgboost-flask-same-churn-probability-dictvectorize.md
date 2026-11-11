---
id: 8c9fc427e2
question: Why do two different customers sometimes get exactly the same churn probability
  from my Flask + XGBoost API (using `DictVectorizer`)?
sort_order: 38
---

Identical predicted probabilities don’t automatically mean your API or model is broken.

With tree-based models like XGBoost, the model splits feature values into ranges using decision thresholds. Two different inputs can still end up taking the exact same path through all trees (even if their raw values differ), which can lead to identical predicted churn probabilities.

At the same time, identical predictions can also be caused by preprocessing mistakes. Here are good checks:

1. Confirm the JSON contains the expected feature names
   Make sure the keys in your incoming JSON match exactly the feature names your training code used.

2. Verify you use the same fitted `DictVectorizer` at training and prediction
   You must load/reuse the already-fitted vectorizer; don’t refit a new one during inference.

3. Compare the transformed vectors for both inputs
   Transform both customer dicts with the fitted `DictVectorizer` and check whether the resulting feature vectors differ.

4. Check whether the differences should change decision paths
   Even if the vectors differ slightly, the tree thresholds might still route both inputs through the same splits, producing the same probability.

Example:

```python
customer_1 = {"age": 35, "balance": 50000}
customer_2 = {"age": 36, "balance": 50500}

X = dv.transform([customer_1, customer_2])
predictions = model.predict_proba(X)[:, 1]

print(predictions)
```

Key takeaway: identical predictions can be a normal outcome of how tree thresholds work, but you should first verify your preprocessing (feature names + using the same fitted `DictVectorizer`) before concluding the model is wrong.