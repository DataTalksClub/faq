---
id: bac852d170
question: 'SQL: Error Column Zone does not exist when selecting from taxi_zones / zones'
sort_order: 21
---

The error happens because the column is named `Zone` with a capital letter, and Postgres folds unquoted identifiers to lowercase.

Quote the column when you query:

```sql
SELECT * FROM zones AS z WHERE z."Zone" = 'Astoria';
```

Or avoid quoting altogether by lowercasing the column names when loading the data. In Pandas, after:

```python
import pandas as pd

df = pd.read_csv('taxi+_zone_lookup.csv')
```

Add:

```python
df.columns = df.columns.str.lower()
```

Also check the value itself: the dataset may have `'Astoria'` instead of `'Astoria Zone'`:

```sql
SELECT * FROM zones AS z WHERE z."Zone" LIKE '%Astoria%';
```
