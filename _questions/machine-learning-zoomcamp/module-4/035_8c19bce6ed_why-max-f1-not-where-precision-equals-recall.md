---
id: 8c19bce6ed
question: Why doesn’t the maximum F1-score happen where precision equals recall (Precision–Recall
  intersection)?
sort_order: 35
---

On an imbalanced classification problem, the threshold where `precision == recall` (or where the two curves intersect) is not guaranteed to maximize the `F1` score.

`F1` is the harmonic mean:

- `F1 = 2 * P * R / (P + R)`

So even if `P` and `R` are close, `F1` can still be lower when the *product* `P * R` is smaller. In practice, changing the decision threshold often shifts precision and recall unevenly:

- At the precision–recall intersection (e.g. `threshold = 0.63`), you may get fairly balanced values (precision and recall close), but the model might still trade away some recall or some precision.
- The threshold that maximizes `F1` (e.g. `threshold = 0.41`) can move you to a different tradeoff: recall may increase a lot while precision decreases. If the recall gain outweighs the precision loss (because `F1` depends strongly on `P * R`), `F1` will be higher even when `P != R`.

In short: balancing `P` and `R` can reduce the gap between metrics, but the `F1` optimum is driven by how the threshold changes the overall `P`/`R` tradeoff—often favoring the metric that improves `P * R` the most (commonly recall on imbalanced datasets).