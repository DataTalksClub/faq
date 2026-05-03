---
id: d2902a7227
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_5924f19e.png
question: 'GCS Bucket - te table: Error while reading data, error message: Parquet
  column ''XYZ'' has type INT which does not match the target cpp_type DOUBLE. File:
  gs://path/to/some/blob.parquet'
sort_order: 2
---

Ultimately, when trying to ingest data into a BigQuery table, all files within a given directory must have the same schema.

When dealing with datasets, such as the FHV Datasets from 2019, you may encounter schema inconsistencies. For example, the files for '2019-05' and '2019-06' have the columns "PUlocationID" and "DOlocationID" as integers, while for the period of '2019-01' through '2019-04', the same columns are defined as floats.

When importing these files as Parquet to BigQuery, the first file will define the table schema. All subsequent files must have the same schema to append data correctly.

<{IMAGE:image_1}>

To prevent errors like this, enforce the data types for the columns on the DataFrame before serializing/uploading them to BigQuery:

```python
pd.read_csv("path_or_url").astype({"col1_name": "datatype", "col2_name": "datatype", ..., "colN_name": "datatype"})
```