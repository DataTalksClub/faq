---
id: 663dda52c8
question: Slightly different RMSE
sort_order: 35
---

**Problem:** My LinearRegression RMSE is very close to the answer but not exactly the same. Is this normal?

**Answer:** No, LinearRegression is a deterministic model; it should always output the same results when given the same inputs.

**Check the Following:**

- Ensure outliers are properly treated in both the train and validation sets.
- Verify that one-hot encoding is correctly applied by inspecting the shape of the one-hot encoded feature matrix. If it shows 2 features, there may be an issue.
  - Hint: Convert drop-off and pick-up codes to the proper data format before fitting with `DictVectorizer`.