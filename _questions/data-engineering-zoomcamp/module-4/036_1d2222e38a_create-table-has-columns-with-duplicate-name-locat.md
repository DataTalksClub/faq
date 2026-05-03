---
id: 1d2222e38a
question: CREATE TABLE has columns with duplicate name locationid.
sort_order: 36
---

This error could result if you are using a `SELECT *` query without specifying the table names.

Example:

```sql
WITH dim_zones AS (
  SELECT * FROM `engaged-cosine-374921`.`dbt_victoria_mola`.`dim_zones`
  WHERE borough != 'Unknown'
),
fhv AS (
  SELECT * FROM `engaged-cosine-374921`.`dbt_victoria_mola`.`stg_fhv_tripdata`
)
SELECT * FROM fhv
INNER JOIN dim_zones AS pickup_zone
ON fhv.PUlocationID = pickup_zone.locationid
INNER JOIN dim_zones AS dropoff_zone
ON fhv.DOlocationID = dropoff_zone.locationid;
```

To resolve, replace with:

```sql
SELECT fhv.* FROM fhv
```
