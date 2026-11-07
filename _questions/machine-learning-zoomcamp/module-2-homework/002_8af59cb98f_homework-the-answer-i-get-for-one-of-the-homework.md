---
id: 8af59cb98f
question: 'Homework: The answer I get for one of the homework questions doesn''t match
  any of the options. What should I do?'
sort_order: 2
---

Select the option closest to your answer. This applies to every cohort: if your value doesn't match any option exactly, pick the closest one. If your value lies between two options, choose the larger one.

**2026 cohort:** the homework uses a pinned dataset (`cohorts/2026/data/`) and the options are computed from it, so your answer should be very close to one option. If it is far from all of them, check these first:

- You downloaded `car_fuel_efficiency_2026.csv` from `cohorts/2026/data/` (not an older car dataset) and kept only the five listed columns.
- You set `np.random.seed(...)` and recreated `idx = np.arange(n)` before every shuffle.
- You computed the imputation mean on `df_train` only.
- You used `np.std` (ddof=0), not pandas `.std()` (ddof=1).
- You rounded as instructed: 3 decimals in Q3, 4 in Q4.

Small differences (library versions, OS, floating point) are normal and not a problem: just pick the closest option.
