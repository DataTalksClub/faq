---
id: d2ffcc91e0
question: 'Can I use GitHub Actions to fetch data, apply an already-trained model and show buy/sell signals for the tickers I follow?'
sort_order: 3
---

Yes. You'd adjust the code slightly - it currently drops rows with unfilled data and doesn't predict the last one-to-three days - but the model can forecast one-to-three days beyond the available data, and you can add a filter to show a specific stock's prediction.
