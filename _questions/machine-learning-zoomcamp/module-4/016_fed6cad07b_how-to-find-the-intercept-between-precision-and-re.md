---
id: fed6cad07b
question: How to find the intercept between precision and recall curves by using numpy?
sort_order: 16
---

You can find the intercept between these two curves using numpy's `diff` and `sign` functions:

1. Ensure your `df_scores` DataFrame is ready with three columns: `threshold`, `precision`, and `recall`.
2. Determine the indices where the precision and recall curves intersect (i.e., where the sign of the difference between precision and recall changes):

   ```python
   import numpy as np

   idx = np.argwhere(
       np.diff(
           np.sign(np.array(df_scores['precision']) - np.array(df_scores['recall']))
       )
   ).flatten()
   ```

3. Print the result to easily read it:

   ```python
   print(f"The precision and recall curves intersect at a threshold equal to {df_scores.loc[idx]['threshold']}.")
   ```