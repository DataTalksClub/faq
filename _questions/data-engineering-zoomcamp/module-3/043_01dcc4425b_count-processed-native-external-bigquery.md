---
id: 01dcc4425b
question: Why does the estimate of Bytes Processed for COUNT(*) stay at 0 bytes on
  a native BigQuery table, but become chargeable with a WHERE filter or when using
  an external table?
sort_order: 43
---

BigQuery's Bytes Processed metric behaves differently depending on the data source and query:

- Native tables (Standard): BigQuery keeps a Metadata Store that already contains the total row_count for the table. For a SELECT COUNT(*), the engine can read the row count from metadata without scanning any data blocks, so the operation is instantaneous and effectively incurs zero bytes processed.
- With a WHERE filter: If you add a predicate (e.g., WHERE fare_amount > 0), BigQuery must read the relevant column blocks to evaluate the condition. You then incur bytes processed proportional to the data scanned for that predicate.
- External tables (GCS): BigQuery has no metadata control over files stored in GCS. To count rows, it must open the Parquet files (or scan the data) to determine the result. The UI may show 0 B before execution, but the actual cost is determined after the query runs because data is read during execution.

Notes:
- If you primarily need the row count and you’re querying a native table, COUNT(*) can be effectively free due to metadata access.
- For filtered or non-native sources, expect bytes processed to reflect the portion of data read during execution.

Example (conceptual):

```sql
-- Counting rows in a native table may not require scanning the data
SELECT COUNT(*) FROM `project.dataset.native_table`;

-- With a filter, data scanned increases
SELECT COUNT(*) FROM `project.dataset.native_table` WHERE fare_amount > 0;

-- For an external table, the count requires reading external Parquet files
SELECT COUNT(*) FROM `project.dataset.external_table`;
```
