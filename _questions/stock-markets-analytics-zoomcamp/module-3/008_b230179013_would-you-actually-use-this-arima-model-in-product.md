---
id: b230179013
question: 'Would you actually use this ARIMA model in production for real trading?'
sort_order: 8
---

No. It underperforms on train/validation and is only positive on test by chance, meaning it's too simple to predict real movements. The instructor would first improve it (automatic parameter selection, more regressors) so the outperformance is consistently above zero before trusting it. It's still useful as an illustrative baseline.
