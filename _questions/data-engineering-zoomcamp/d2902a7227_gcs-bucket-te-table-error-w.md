---
id: d2902a7227
question: GCS Bucket - te table: Error while reading data, error message: Parquet column 'XYZ' has type INT which does not match the target cpp_type DOUBLE. File: gs://path/to/some/blob.parquet
section: Module 3: Data Warehousing
course: data-engineering-zoomcamp
sort_order: 2000
---

Ultimately, when trying to ingest data into a BigQuery table, all files within a given directory must have the same schema.

When dealing for example with the FHV Datasets from 2019, however (see image below), one can see that the files for '2019-05', and 2019-06, have the columns "PUlocationID" and "DOlocationID" as Integers, while for the period of '2019-01' through '2019-04', the same column is defined as FLOAT.parquet

So while importing these files as parquet to BigQuery, the first one will be used to define the schema of the table, while all files following that will be used to append data on the existing table. Which means, they must all follow the very same schema of the file that created the table.

![Image](images/data-engineering-zoomcamp/image_5924f19e.png)

So, in order to prevent errors like that, make sure to enforce the data types for the columns on the DataFrame before you serialize/upload them to BigQuery. Like this:

pd.read_csv("path_or_url").astype({
	"col1_name": "datatype",	
	"col2_name": "datatype",	
	...					
	"colN_name": "datatype" 	
})

