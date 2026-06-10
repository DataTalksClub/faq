---
id: ac9288e96d
question: 'How did you choose the ARIMA parameters (2,1,2) - cross-validation or common sense?'
sort_order: 5
---

Mostly common sense: the differencing term (I) had to be greater than zero because the series has a growing trend and the model won't converge on non-stationary data, and the AR and MA orders were kept small to avoid overfitting. There is an auto-ARIMA implementation for automatic selection, but it needs additional statistical tests and is more complicated to do properly.
