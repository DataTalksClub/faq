---
id: 1ecf8f6d71
question: 'My modeling DataFrame has 300+ feature columns. How do I manage that?'
sort_order: 1
---

Expand the number of tickers rather than splitting the data into separate frames - splitting loses the relationships between technical and macro features. For large datasets, use a powerful machine with GPU-accelerated Pandas (cudf) and GPU ML implementations, since hyperparameter tuning gets heavy (that is why it is out of scope for the course). Dropping the ticker dummy variables makes the model more generic but less precise per stock.
