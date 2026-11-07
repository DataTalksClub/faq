---
id: 322f24380b
question: Do I need to scale/standardize features before training a Decision Tree
  or Random Forest?
sort_order: 32
---

No. Tree-based models split on thresholds (e.g. `x > t`), so they are invariant to monotonic transformations of a feature, including scaling/standardization.

Scaling changes the numeric value of the threshold but not the ordering of samples, so the same types of splits are still available. That means you can skip `StandardScaler` for Decision Trees and Random Forests.

Notes:
- This is different from distance- or gradient-based models (kNN, SVM, logistic regression, neural nets), where feature scale affects the objective and training, so scaling is typically needed.
- Missing values still need handling (e.g., impute with median/mode for scikit-learn Random Forests, or use models that can handle nulls natively like XGBoost/LightGBM/CatBoost).
- Categorical features still need encoding (e.g., one-hot for low cardinality; native handling in CatBoost/LightGBM for higher cardinality). Scaling does not replace encoding.