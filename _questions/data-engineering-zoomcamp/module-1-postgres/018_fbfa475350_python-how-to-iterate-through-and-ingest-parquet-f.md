---
id: fbfa475350
question: 'Python: How to iterate through and ingest parquet file'
sort_order: 18
---

Contrary to pandas’ `read_csv` method, there’s no simple way to iterate through and set chunksize for parquet files. We can use PyArrow (Apache Arrow Python bindings) to resolve that.

```python
import pyarrow.parquet as pq
from sqlalchemy import create_engine
import time

output_name = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

parquet_file = pq.ParquetFile(output_name)
parquet_size = parquet_file.metadata.num_rows

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

table_name = "yellow_taxi_schema"

# Clear table if exists
pq.read_table(output_name).to_pandas().head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

# Default (and max) batch size
index = 65536

for i in parquet_file.iter_batches(use_threads=True):
    t_start = time.time()
    print(f'Ingesting {index} out of {parquet_size} rows ({index / parquet_size:.0%})')
    i.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')
    index += 65536
    t_end = time.time()
    print(f'\t- it took %.1f seconds' % (t_end - t_start))
```