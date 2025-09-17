---
course: data-engineering-zoomcamp
id: 45bd267149
question: “Parquet column 'ehail_fee' has type DOUBLE which does not match the target
  cpp_type INT64”
section: 'Module 4: analytics engineering with dbt'
sort_order: 2530
---

Reason: Parquet files have their own schema. Some parquet files for green data have records with decimals in ehail_fee column.

There are some possible fixes:

Drop ehail_feel column since it is not really used. For instance when creating a partitioned table from the external table in BigQuery

SELECT * EXCEPT (ehail_fee) FROM…

Modify stg_green_tripdata.sql model using this line cast(0 as numeric) as ehail_fee.

Modify Airflow dag to make the conversion and avoid the error.

pv.read_csv(src_file, convert_options=pv.ConvertOptions(column_types = {'ehail_fee': 'float64'}))

Same type of ERROR - parquet files with different data types - Fix it with pandas

Here is another possibility that could be interesting:

You can specify the dtypes when importing the file from csv to a dataframe with pandas

pd.from_csv(..., dtype=type_dict)

One obstacle is that the regular int64 pandas use (I think this is from the numpy library) does not accept null values (NaN, not a number). But you can use the pandas Int64 instead, notice capital ‘I’. The type_dict is a python dictionary mapping the column names to the dtypes.

Sources:

