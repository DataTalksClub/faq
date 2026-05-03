---
id: d677df9ccb
question: 'Taxi Data: How to handle *.csv.gz taxi data files?'
sort_order: 2
---

In [this video](https://www.youtube.com/watch?v=B1WwATwf-vY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb), the data file is stored as `output.csv`. If the file extension is `csv.gz` instead of `csv`, it won't store correctly.

To handle this:

1. Replace `csv_name = "output.csv"` with the file name extracted from the URL. For example, for the yellow taxi data, use:
   
   ```python
   url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
   csv_name = url.split("/")[-1]
   ```

2. When you use `csv_name` with `pandas.read_csv`, it will work correctly because `pandas.read_csv` can directly read files with the `csv.gz` extension.

Example:

```python
import pandas as pd

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
csv_name = url.split("/")[-1]

data = pd.read_csv(csv_name)
```