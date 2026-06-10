---
id: 807e0a519b
question: 'How do I compute the future growth columns (growth_future_1d ... growth_future_30d) efficiently?'
sort_order: 1
---

Use vectorized operations with .shift() rather than looping over rows. Keep in mind that stock data is business days only, so use .shift(i) (not a calendar timedelta), use Adj.Close, and account for the lag between an IPO date and the first day price data is actually available. The Module 2 notebook's loop that defines many columns at once is a good template.
