---
id: 34ebc2c6de
question: TypeError when using spark.createDataFrame function on a pandas df
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3650
---

Error:

spark.createDataFrame(df_pandas).schema

TypeError: field Affiliated_base_number: Can not merge type <class 'pyspark.sql.types.StringType'> and <class 'pyspark.sql.types.DoubleType'>

Solution:

Affiliated_base_number is a mix of letters and numbers (you can check this with a preview of the table), so it cannot be set to DoubleType (only for double-precision numbers). The suitable type would be StringType. Spark  inferSchema is more accurate than Pandas infer type method in this case. You can set it to  true  while reading the csv, so you don’t have to take out any data from your dataset. Something like this can help:

df = spark.read \

.options(

header = "true", \

inferSchema = "true", \

) \

.csv('path/to/your/csv/file/')

Solution B:

It's because some rows in the affiliated_base_number are null and therefore it is assigned the datatype String and this cannot be converted to type Double. So if you really want to convert this pandas df to a pyspark df only take the  rows from the pandas df that are not null in the 'Affiliated_base_number' column. Then you will be able to apply the pyspark function createDataFrame.

# Only take rows that have no null values

pandas_df= pandas_df[pandas_df.notnull().all(1)]

