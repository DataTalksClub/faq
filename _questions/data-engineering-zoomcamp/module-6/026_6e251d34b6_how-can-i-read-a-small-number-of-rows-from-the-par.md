---
id: 6e251d34b6
question: How can I read a small number of rows from the parquet file directly?
sort_order: 26
---

To read a small number of rows from a parquet file, you can use PyArrow or Apache Spark:

### Using PyArrow

```python
from pyarrow.parquet import ParquetFile

pf = ParquetFile('fhvhv_tripdata_2021-01.parquet')

# PyArrow builds tables, not dataframes

tbl_small = next(pf.iter_batches(batch_size=1000))

# Convert the table to a DataFrame

df = tbl_small.to_pandas()
```

### Alternatively, without PyArrow

```python
df = spark.read.parquet('fhvhv_tripdata_2021-01.parquet')

df1 = df.sort('DOLocationID').limit(1000)

pdf = df1.select("*").toPandas()
```