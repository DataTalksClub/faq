---
id: fca91fa9b2
question: "Should the trading simulation buy at the next day's open or at the close?"
sort_order: 2
---

It depends on your trading workflow. If you decide on trades before the market opens, you only know the previous Close, so you trade on Close. If you trade after the market opens, redefine the growth variables on the Open prices (with the correct shift/lag) so the simulation reflects what you can actually execute. Be careful with realtime data lag (free sources like yfinance can lag 15-20 minutes).
