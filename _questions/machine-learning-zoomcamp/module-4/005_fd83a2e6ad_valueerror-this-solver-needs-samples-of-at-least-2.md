---
id: fd83a2e6ad
question: 'ValueError: This solver needs samples of at least 2 classes in the data,
  but the data contains only one class: 0'
sort_order: 5
---

This error indicates that your dataset's `churn` column only contains the class `0`, but at least two classes are required.


1. Check your data processing steps where binary conversion might be applied. Specifically, ensure that the line:
   
   ```python
   df.churn = (df.churn == 'yes').astype(int)
   ```
   
   is operating correctly. Verify that there are indeed records where `churn` should evaluate to `1` (i.e., cases where `churn` equals `'yes'`).

2. If all values are `0`, make sure your original dataset and preprocessing steps are correctly implemented to represent cases with both classes (`0` and `1`).

3. Review data preprocessing steps and confirm the filtering, transformation, or data importing steps do not inadvertently drop or misclassify the non-zero class records.

This should resolve the error by ensuring your data contains at least one record for each class.