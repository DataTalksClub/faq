---
id: 8af59cb98f
question: Is there any reason for the slightly different RMSE result when doing the
  Q2 in Homework 6?
sort_order: 2
---

Slight RMSE differences usually come from evaluating on data that isn’t exactly the same as what the homework expects—most commonly, using the full dataframe (`df`) instead of the training split (`df_train`) when fitting the preprocessing/imputation.

Concretely:
- For imputation/transformers that learn from data, fit them on `df_train` (e.g., `dv.fit(df_train)`), then transform `df_train`/`df_val`/`df_test` using that fitted object.
- Don’t fit on the full dataset (`dv.fit(df)`), because that leaks information from validation/test into training and will change downstream metrics (so Q3/Q4 can also shift).

Also re-check the exact rounding/standardization steps the homework specifies; if everything matches but you still see a tiny difference, small floating-point/library-version differences can happen—pick the closest option.