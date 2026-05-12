---
id: 7f18a34896
question: How can I work with very large datasets, e.g. the New York Yellow Taxi dataset,
  with over a million rows?
sort_order: 28
---

You can consider several different approaches:

- **Sampling**: In the exploratory phase, you can use random samples of the data.

- **Chunking**: When you do need all the data, you can read and process it in chunks that do fit in the memory.

- **Optimizing data types**: Pandas’ automatic data type inference (when reading data in) might result in, e.g., `float64` precision being used to represent integers, which wastes space. You might achieve substantial memory reduction by optimizing the data types.

- **Using Dask**: An open-source Python project which parallelizes Numpy and Pandas.

See, e.g., [this blog on Vantage AI](https://www.vantage-ai.com/en/blog/4-strategies-how-to-deal-with-large-datasets-in-pandas)