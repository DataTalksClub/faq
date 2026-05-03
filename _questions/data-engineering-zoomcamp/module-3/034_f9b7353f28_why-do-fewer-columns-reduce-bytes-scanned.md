---
id: f9b7353f28
question: Why does selecting fewer columns reduce the number of bytes scanned?
sort_order: 34
---

BigQuery uses columnar storage, so only the columns referenced in a query are read during execution. Selecting fewer columns directly reduces the amount of data scanned and therefore lowers query cost.