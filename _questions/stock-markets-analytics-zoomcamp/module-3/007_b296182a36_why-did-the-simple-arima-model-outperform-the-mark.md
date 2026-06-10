---
id: b296182a36
question: 'Why did the simple ARIMA model outperform the market on the test set - was it just luck?'
sort_order: 7
---

Largely luck. The model trained on a period of high growth, so its coefficients heavily weight recent upward movements and it over-predicts growth, which happened to match the very strong last few years. The instructor considers this outperformance suspicious rather than a sign of a genuinely good model.
