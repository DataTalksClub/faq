---
id: bcafec775a
question: How many records are stored in each partition/parquet file when writing
  a Spark DataFrame with repartition?
sort_order: 31
---

When you repartition a DataFrame and write it to Parquet, Spark writes one Parquet file per partition. The total number of rows in the dataset is distributed across those files, so each partition file contains roughly N / num_partitions rows (where N is the total row count and num_partitions is the number of partitions you repartitioned to). The exact counts per file depend on the data distribution and the chosen number of partitions.

Example:
```
df.repartition(4).write.parquet("output/")
```

To see how many rows are in each partition file, read the output and count rows per input file:
```
spark.read.parquet("output/").groupBy(input_file_name()).count().show()
```

Notes:
- The function `input_file_name()` helps identify which file a row came from. You may need to import it in PySpark:
```
from pyspark.sql.functions import input_file_name
```
- The counts shown by the above command correspond to the quiz options, and will vary with dataset size and the number of partitions you write to. If you want more uniform file sizes, adjust the number of partitions or use `coalesce`/`repartition` as appropriate.
