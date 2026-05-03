---
id: e0c1900c47
question: 'Python: Pandas can read *.csv.gzip'
sort_order: 17
---

When a CSV file is compressed using Gzip, it is saved with a ".csv.gz" file extension. This file type is also known as a Gzip compressed CSV file. To read a Gzip compressed CSV file using Pandas, you can use the `read_csv()` function.

Here is an example of how to read a Gzip compressed CSV file using Pandas:

```python
import pandas as pd

df = pd.read_csv('file.csv.gz',
                 compression='gzip',
                 low_memory=False)
```