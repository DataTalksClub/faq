---
id: 6f04719ff8
question: Why does max(trip_distance) return extremely large values in Spark for yellow_tripdata_2023-11,
  and how can I obtain a realistic maximum?
sort_order: 32
---

- This issue is caused by data quality problems in the NYC Taxi dataset. Some rows have unrealistic trip_distance values due to GPS errors, sensor faults, corrupted trip records, or incorrect meter readings. When Spark computes max(trip_distance) without filtering, these outliers inflate the result.

- To obtain a more realistic maximum, apply a simple filter before computing the maximum. For example:

```python
df.filter('trip_distance > 0 AND trip_distance < 200').selectExpr('max(trip_distance)').show()
```

- Notes:
  - The threshold (200 in the example) is dataset-specific; adjust it to reflect plausible trip distances for your data.
  - This approach helps you reflect typical taxi trips rather than including extreme outliers.
