---
id: 6b4bd387cf
question: Why does the PyFlink streaming job fail with a JSON deserialization error
  when consuming records from the Kafka/Redpanda topic?
sort_order: 29
---

Problem
The PyFlink streaming job fails during deserialization with a JSON error when consuming records from Kafka/Redpanda. This happens if the produced JSON payload contains NaN values (e.g., NaN in numeric fields like passenger_count). Standard JSON does not allow NaN, so Flink's JSON parser rejects the payload and the source fails, causing the job to restart.

Root cause
NaN is not valid JSON. When NaN is serialized into JSON, downstream JSON parsers (including Flink's) fail to parse the record.

Fix
Clean the dataset before producing events by replacing NaN values with null or a valid number before serialization.

How to implement (example in Python)
```python
import json
import math

def sanitize_and_serialize(record):
    # Convert NaNs to JSON nulls
    for key, value in record.items():
        if isinstance(value, float) and math.isnan(value):
            record[key] = None
    return json.dumps(record, separators=(',', ':'), ensure_ascii=False)

# Example usage
# Suppose 'rows' is an iterable of dicts representing taxi trips
for row in rows:
    json_str = sanitize_and_serialize(row)
    # send json_str to Kafka/Redpanda
```

Alternative: simple NaN handling with a default numeric value
```python
# If you prefer numeric defaults instead of nulls
df = df.fillna({'passenger_count': 0, 'trip_distance': 0, 'fare_amount': 0})
```

Validation
- After serialization, verify that the payload is valid JSON:
```python
import json
json.loads(json_str)  # should not raise
```

Notes
- This is the recommended approach; avoid sending NaN in JSON payloads.
- If you cannot modify the producer, you may consider additional validation at the ingestion layer, but the source-level sanitization is most reliable.
