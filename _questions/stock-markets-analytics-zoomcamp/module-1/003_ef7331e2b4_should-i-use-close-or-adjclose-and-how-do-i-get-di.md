---
id: ef7331e2b4
question: 'Should I use Close or Adj.Close, and how do I get dividends?'
sort_order: 3
---

Use Adj.Close for computing returns - it avoids the artificial price jumps on dividend dates. The old difference between Close and Adj.Close is effectively deprecated (the API now returns only Close), and for dividends you should use Yahoo Finance's dividend data rather than deriving it from the price difference.
