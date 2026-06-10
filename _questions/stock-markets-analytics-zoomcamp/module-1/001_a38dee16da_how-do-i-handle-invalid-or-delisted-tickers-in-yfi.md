---
id: a38dee16da
question: 'How do I handle invalid or delisted tickers in yfinance (e.g. "No timezone found, symbol may be delisted")?'
sort_order: 1
---

The ticker may be delisted or may have changed symbol - check ticker changes at stockanalysis.com/actions/changes (for example PTHR became HOVR, and some need a different suffix like PTHR -> PTHRF). Also note yfinance only validates a ticker when you actually call the API (not when you create the Ticker object), so check the data you receive rather than assuming the object is valid.
