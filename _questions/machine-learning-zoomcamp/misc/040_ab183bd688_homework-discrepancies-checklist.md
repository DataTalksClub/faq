---
id: ab183bd688
question: 'My homework answer doesn''t match any of the options'
sort_order: 40
---

Common causes, in order of frequency:

1. Wrong column slice or filter — apply filters BEFORE selecting columns / `.head(n)` / `.values`.
2. Log transform applied where it shouldn't be (or not applied where it should).
3. Rounding too early — only round the final answer, not intermediate values, unless explicitly told to.
4. Different sklearn / numpy / Python versions — pin them via `requirements.txt`, `Pipfile.lock`, or `uv.lock`.
5. Different train/val/test split logic — `train_test_split` shuffles by default; manual `np.random.shuffle` produces a different ordering than sklearn's.

If your answer still doesn't match after these checks:

- **2026 cohort:** the options are computed from a pinned data release, and the homework says not to choose a merely close value. A mismatch means something in your code differs from the instructions, so re-check your work (data file, split, seeds, rounding) rather than picking the nearest option.
- **Older cohorts:** pick the closest option.
