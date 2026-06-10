---
id: c84ca86bdb
question: 'Does the trained model require trading the exact same set of stocks in production?'
sort_order: 1
---

Yes - the model assumes the set of stocks it was trained on. It will still work on other stocks, just less accurately (ticker dummies are usually not among the strongest factors). The recommendation is to include all the stocks you actually want to invest in when you train, and to compare the train/test/validation distributions of your outcome and features.
