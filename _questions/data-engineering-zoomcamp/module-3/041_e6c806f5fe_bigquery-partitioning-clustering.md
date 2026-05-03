---
id: e6c806f5fe
question: How do you partition and cluster a table in BigQuery for better performance?
sort_order: 41
---

Overview:
- Partitioning reduces scanned data by dividing a table into smaller parts based on a column used in WHERE clauses.
- Clustering organizes data within partitions by one or more columns, improving the performance of ORDER BY and range queries. Note: BigQuery supports partitioning by only one column, but you can cluster on multiple columns.

Best practices:
- Partition based on the column you filter on most frequently in WHERE clauses.
- Cluster within partitions by columns used in ORDER BY to optimize data retrieval inside each partition.

Examples:

```sql
-- Partitioned by DATE(tpep_dropoff_datetime) and clustered by VendorID
CREATE OR REPLACE TABLE `nyc_taxi_data.yellow_tripdata_id_clustered`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `nyc_taxi_data.yellow_tripdata_ext`;
```

```sql
-- Partitioned on VendorID and clustered by tpep_dropoff_datetime
CREATE OR REPLACE TABLE `nyc_taxi_data.yellow_tripdata_date_clustered`
PARTITION BY RANGE_BUCKET(VendorID, GENERATE_ARRAY(0, 100, 1))
CLUSTER BY tpep_dropoff_datetime
AS
SELECT * FROM `nyc_taxi_data.yellow_tripdata_ext`;
```

```sql
-- Clustering on two columns (VendorID and tpep_dropoff_datetime)
CREATE OR REPLACE TABLE `nyc_taxi_data.yellow_tripdata_date_id_clustered`
CLUSTER BY VendorID, tpep_dropoff_datetime
AS
SELECT * FROM `nyc_taxi_data.yellow_tripdata_ext`;
```

Filtering behavior (conceptual):
- When a query filters on the partitioned column (e.g., VendorID in a table partitioned by VendorID), the engine can prune partitions and process only the relevant data (often much smaller scans).
- When a query filters on the partitioned column but the table is partitioned differently (e.g., by date), the engine may scan more data, potentially the entire table, depending on the partitioning scheme and data distribution.

For example, in the provided scenarios:
- A table partitioned by VendorID and clustered by tpep_dropoff_datetime may process a very small portion of data when filtering on a single VendorID value.
- A table partitioned by tpep_dropoff_datetime and clustered by VendorID may scan a larger portion of the data if the VendorID value exists across many partitions.

Notes:
- BigQuery supports only one partitioning column per table.
- You can combine partitioning with clustering (on one or more columns) to optimize specific query patterns.

If you have a dataset you want to optimize, start by identifying the most selective filter column for partitioning, then choose clustering keys that support your common ORDER BY or range queries.