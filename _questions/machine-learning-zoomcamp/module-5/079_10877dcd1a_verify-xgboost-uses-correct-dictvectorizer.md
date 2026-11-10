---
id: 10877dcd1a
question: How can I verify that my deployed XGBoost model is using the correct saved
  `DictVectorizer`?
sort_order: 79
---

When serving an XGBoost model that relies on `DictVectorizer`, you need to ensure the encoder you load in production is the *same fitted* one used during training. A common failure mode is deploying an older `dv.bin`, which can change the encoded feature matrix (feature order/names and sometimes the set of active features), leading to incorrect predictions.

Practical way to verify:

1. Save the fitted `DictVectorizer` and the trained XGBoost model together (from the same training run).
2. In your prediction service, load both artifacts.
3. Compare compatibility using the fitted encoder output schema:
   - Get the encoder’s expected feature names via `dv.get_feature_names_out()` (and optionally its length).
   - Ensure the serving-time encoding uses that same fitted `dv` (avoid refitting the `DictVectorizer` at prediction time).
4. Sanity-check with an identical sample input:
   - Run the same raw record through the same `dv` to build the model input.
   - Compare predictions between your original environment and your deployed container/service.

Important: matching only the feature count is not sufficient—different vectorizers can still produce the same number of features with different feature names/ordering. For stronger assurance, also verify the expected feature names (or persist a version/manifest of `dv` features alongside the model artifacts).