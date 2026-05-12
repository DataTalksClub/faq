---
id: fa12df76a7
question: 'Mage error: TypeError: string indices must be integers'
sort_order: 14
---

If you've removed and re-added blocks (especially while debugging Global Data Products), the upstream connections may be stale.

- Remove the connections from the `hyperparameter_tuning/sklearn` block in the Tree panel to its upstream blocks.
- Re-add these connections.
- Save the pipeline with `Ctrl+S`.
