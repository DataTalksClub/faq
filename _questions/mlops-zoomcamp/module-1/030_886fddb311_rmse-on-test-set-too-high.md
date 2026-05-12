---
id: 886fddb311
question: RMSE on test set too high
sort_order: 30
---

RMSE on the test set was too high when hot encoding the validation set using a previously fitted `OneHotEncoder(handle_unknown='ignore')` on the training set. In contrast, `DictVectorizer` yielded the correct RMSE.

In principle, both transformers should behave identically when treating categorical features, especially in scenarios where there are no sequences of strings in each row (as in this week’s homework):

- Features are put into binary columns encoding their presence (1) or absence (0).
- Unknown categories are imputed as zeros in the hot-encoded matrix.

This discrepancy indicates that there might be a difference in how `OneHotEncoder` and `DictVectorizer` handle the data after fitting on the training set and applying to the validation set.