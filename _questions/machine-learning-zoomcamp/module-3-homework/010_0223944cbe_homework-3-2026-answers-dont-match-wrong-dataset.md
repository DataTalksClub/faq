---
id: 0223944cbe
question: 'Homework 3 (2026): Why don''t my answers match any option?'
sort_order: 10
---

First check that you're using the pinned 2026 dataset:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/main/cohorts/2026/data/course_lead_scoring_2026.csv
```

The 2025 cohort used a file with the same name pattern and the **same columns** (`alexeygrigorev/datasets/.../course_lead_scoring.csv`), so loading it raises no error, but it has different rows and gives different answers. Check with `len(df)`: the 2026 file has 5,000 rows.

The target is `converted`. If you see `KeyError: 'churn'` or `'tenure'`, you copied code from the churn lecture notebook without adapting the column names.

Then make sure you follow the homework exactly:

- fill missing categorical values with `'NA'` and numerical values with `0.0`
- split with `random_state=42` in both calls:

  ```python
  df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
  df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)
  ```

- remove `converted` from the feature dataframes after splitting

The 2026 options are computed from the pinned release, so with the right file your results should match an option exactly.

Homework: [cohorts/2026/homework/03-classification](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/main/cohorts/2026/homework/03-classification)
