---
id: 7f18a34896
question: How can I work with very large datasets, e.g. the New York Yellow Taxi dataset, with over a million rows?
section: Miscellaneous
course: machine-learning-zoomcamp
sort_order: 4210
---

You can consider several different approaches:

Sampling: In the exploratory phase, you can use random samples of the data.

Chunking: When you do need all the data, you can read and process it in chunks that do fit in the memory.

Optimizing data types: Pandas’ automatic data type inference (when reading data in) might result in e.g. float64 precision being used to represent integers, which wastes space. You might achieve substantial memory reduction by optimizing the data types.

Using Dask, an open-source python project which parallelizes Numpy and Pandas.

(see, e.g. )

By Rileen Sinha

