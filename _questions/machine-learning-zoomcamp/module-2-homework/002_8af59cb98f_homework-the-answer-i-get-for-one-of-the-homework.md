---
id: 8af59cb98f
question: 'Homework: The answer I get for one of the homework questions doesn''t match
  any of the options. What should I do?'
sort_order: 2
---

**2026 cohort:** don't pick a close option. The homework uses a pinned dataset (`cohorts/2026/data/`), and the options are computed from it, so a mismatch means a bug. Check these first:

- You downloaded `car_fuel_efficiency_2026.csv` from `cohorts/2026/data/` (not an older car dataset) and kept only the five listed columns.
- You set `np.random.seed(...)` and recreated `idx = np.arange(n)` before every shuffle.
- You computed the imputation mean on `df_train` only.
- You used `np.std` (ddof=0), not pandas `.std()` (ddof=1).
- You rounded as instructed: 3 decimals in Q3, 4 in Q4.

**Older cohorts:** environments differ, so select the option closest to your answer. If your value lies between two options, choose the larger one.
