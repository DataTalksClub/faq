---
id: 3e355d74fd
question: DataType error when creating Spark DataFrame with a specified schema?
sort_order: 27
---

When defining the schema for a Spark DataFrame, you might encounter a data type error if you're using a Parquet file with the schema definition from the TLC example. The error occurs because the `PULocationID` and `DOLocationID` columns are defined as `IntegerType`, but the Parquet file uses `INT64`.

You'll get an error like:

```plaintext
Parquet column cannot be converted in file [...] Column [...] Expected: int, Found: INT64
```

To resolve this issue:

- Change the schema definition from `IntegerType` to `LongType`. This adjustment should align the expected and actual data types, allowing the DataFrame to be created successfully.