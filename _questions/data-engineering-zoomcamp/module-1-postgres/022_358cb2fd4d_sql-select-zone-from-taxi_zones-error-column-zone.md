---
id: 358cb2fd4d
question: 'SQL: SELECT Zone FROM taxi_zones Error Column Zone doesn''t exist'
sort_order: 22
---

It is inconvenient to use quotation marks all the time, so it is better to put the data in the database all in lowercase. In Pandas, after:

```python
import pandas as pd

df = pd.read_csv('taxi+_zone_lookup.csv')
```

Add the row:

```python
df.columns = df.columns.str.lower()
```