---
course: data-engineering-zoomcamp
id: fbfa475350
question: Python - How to iterate through and ingest parquet file
section: 'Module 1: Docker and Terraform'
sort_order: 1350
---

Contrary to panda’s read_csv method there’s no such easy way to iterate through and set chunksize for parquet files. We can use PyArrow (Apache Arrow Python bindings) to resolve that.

import pyarrow.parquet as pq

output_name = “”

parquet_file = pq.ParquetFile(output_name)

parquet_size = parquet_file.metadata.num_rows

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

table_name=”yellow_taxi_schema”

# Clear table if exists

pq.read_table(output_name).to_pandas().head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

# default (and max) batch size

index = 65536

for i in parquet_file.iter_batches(use_threads=True):

t_start = time()

print(f'Ingesting {index} out of {parquet_size} rows ({index / parquet_size:.0%})')

i.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')

index += 65536

t_end = time()

print(f'\t- it took %.1f seconds' % (t_end - t_start))

