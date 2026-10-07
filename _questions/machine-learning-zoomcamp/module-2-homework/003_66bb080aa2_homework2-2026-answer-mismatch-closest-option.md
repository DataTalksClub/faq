---
id: 66bb080aa2
question: 'Homework 2 (2026): My answer doesn’t exactly match any option—can I pick
  the closest one?'
sort_order: 3
---

No—you should not pick the closest option for the 2026 cohort. Homework 2 uses a pinned, checksummed dataset (`cohorts/2026/data/`), and the instructions require you to use the value that matches your calculation exactly. A mismatch usually indicates a bug in your code.

Common causes:
- Not setting the seed with `np.random.seed()`.
- Computing the imputation mean on the full dataset instead of using only `df_train`.
- Not recreating `idx = np.arange(n)` before each shuffle.
- Using `pandas.DataFrame.std()` (with `ddof=1`) instead of `np.std` (which uses `ddof=0`).
- Rounding to the wrong number of decimals (e.g., Q3 uses 3 decimals and Q4 uses 4).

The “pick the closest option” advice applies to older cohorts where the dataset wasn’t pinned.