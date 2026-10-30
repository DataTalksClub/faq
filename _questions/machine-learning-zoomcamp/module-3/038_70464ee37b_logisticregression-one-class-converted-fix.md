---
id: 70464ee37b
question: 'LogisticRegression fails with “This solver needs samples of at least 2
  classes… but the data contains only one class” when training on `course_lead_scoring_2026.csv`:
  how do I fix it?'
sort_order: 38
---

This error means your training labels (for example `y_train` from the `converted` column) contain only a single class (all `0`s or all `1`s). `LogisticRegression` requires at least two classes to learn.

Check for these common data-preparation mistakes:

- Target overwritten during imputation:
  - If you accidentally included `converted` in the list of numerical features and then ran something like `.fillna(0.0)`, you can overwrite the target values and end up with only zeros.
  - Fix: when building your numeric feature list, explicitly exclude `converted`.

- Target deleted too early:
  - If you dropped `converted` (e.g. `del df_train['converted']`) before extracting `y_train`, you may end up training with a wrong/empty label vector.
  - Fix: extract `y_train = df_train['converted']` first, then drop `converted` from the feature dataframe.

A safe pattern is:

```python
# df is your full dataframe
numerical = [c for c in df.select_dtypes(include=['number']).columns if c != 'converted']

# ... build X from numerical columns, and create y from the target
X_train = df_train[numerical]
y_train = df_train['converted'].values
```

After your preprocessing, verify the label distribution:

```python
import numpy as np
print(np.unique(y_train, return_counts=True))
```

You should see counts for both classes (at least one `0` and at least one `1`).