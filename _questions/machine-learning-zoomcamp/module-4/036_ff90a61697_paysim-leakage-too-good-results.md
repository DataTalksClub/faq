---
id: ff90a61697
question: My model gets extremely high PR-AUC/accuracy on the PaySim synthetic fraud
  dataset—am I hitting a dataset-specific leakage trap?
sort_order: 36
---

If your PR-AUC/accuracy looks “too good” on PaySim, the most common cause is feature leakage: some balance columns effectively encode whether the transfer was cancelled as fraud.

On PaySim, a fraudulent transfer is cancelled once it’s flagged. That means the post-transaction balance columns carry the outcome:

- `oldbalanceOrg`: balance before the transfer
- `newbalanceOrig`: balance after
- `oldbalanceDest`, `newbalanceDest`: same idea for the recipient

For legitimate transfers, the arithmetic holds: `newbalanceOrig == oldbalanceOrg - amount`.
For cancelled (fraudulent) ones, it typically does not. As a result, the “balance inconsistency” becomes a near-direct copy of the label.

What to do:

1. Drop `newbalanceOrig` and `newbalanceDest` from your features.
2. Keep `oldbalanceOrg` / `oldbalanceDest` only as pre-transaction features (they are known before the transaction).
3. Never create features that compare “before vs after” balances (e.g., anything derived from `newbalance*`).

A leak-free feature you can use is:

- `balance_after_send = oldbalanceOrg - amount`

You can sanity-check for leakage by training two versions: one including the balance-after columns and one with them removed. If the score barely moves, you didn’t leak. If it collapses, you did, and your original metrics were not meaningful.