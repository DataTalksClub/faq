---
id: 8d6a161b65
question: 'Should I build one model per stock, or a single model covering all stocks?'
sort_order: 9
---

It's a hard, open question with no clear answer. A deep neural network tends to generalize better with more data (e.g. 50-100 tickers giving a million rows instead of a few thousand), but a model trained on a single stock may work better specifically for that stock. Try both and compare.
