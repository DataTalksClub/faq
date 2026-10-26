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

If your answer still doesn't match exactly after these checks, pick the closest option. This applies to all cohorts, including 2026.

If your answer is far from every option, something in your code most likely differs from the instructions (data file, split, seeds, rounding), so it's worth re-checking. But small differences are expected: always choose the closest option.
