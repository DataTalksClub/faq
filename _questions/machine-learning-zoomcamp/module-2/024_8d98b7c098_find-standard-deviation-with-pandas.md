---
id: 8d98b7c098
question: Find standard deviation with Pandas
sort_order: 24
---

To find the standard deviation of a list or series of data using Pandas, you can convert the list into a Pandas Series and use the `.std()` function. For example:

```python
import pandas as pd

x = [1, 2, 3, 4, 5]
standard_deviation = pd.Series(x).std()
print(standard_deviation)
```

This will calculate the standard deviation of the list `x`.

For a DataFrame column, use:

```python
df['column_name'].std()
```

It also works on several columns at once:

```python
df[['column_1', 'column_2']].std()
```