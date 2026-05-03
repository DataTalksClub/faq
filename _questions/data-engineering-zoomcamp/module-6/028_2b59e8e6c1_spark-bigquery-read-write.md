---
id: 2b59e8e6c1
question: How do I use Spark with BigQuery as a data source and sink?
sort_order: 28
---

Add the connector package: `com.google.cloud.spark:spark-bigquery-with-dependencies_2.12` 

Read from BigQuery:

```python
df = spark.read.format("bigquery") \
.option("table", "project.dataset.table") \
.load()
```

Write to BigQuery:

```python
df.write.format("bigquery") \
.option("table", "project.dataset.output_table") \
.mode("overwrite") \
.save()
```

Make sure:
- your GCP credentials are configured
- dataset location matches your query location
- the output dataset exists

This enables distributed processing on top of warehouse data.
