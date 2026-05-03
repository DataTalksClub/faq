---
id: 1da0437718
question: How can I calculate the duration between two Spark timestamp columns in
  hours (e.g., tpep_pickup_datetime and tpep_dropoff_datetime)?
sort_order: 23
---

You can compute the duration in hours between two Spark timestamp columns in several ways. Choose the approach that best fits your workflow:

- Using unix_timestamp (per-row hours as a floating-point value):
````python
from pyspark.sql import functions as F

trip_duration_hours = (
    F.unix_timestamp("tpep_dropoff_datetime") -
    F.unix_timestamp("tpep_pickup_datetime")
) / 3600
````
This yields the duration in hours for each row as a numeric value.

- Using datediff (hours approximation via days):
````python
from pyspark.sql import functions as F

# difference in days, then multiply by 24 to get hours
hours = F.datediff("tpep_dropoff_datetime", "tpep_pickup_datetime") * 24
````
Note that datediff returns whole days; if you need sub-day precision, prefer the unix_timestamp method above or compute seconds directly.

- Working with Python timedelta after collecting (Python-side calculation):
````python
# after collecting to Python (e.g., with toPandas or collect):
# delta is a Python datetime.timedelta object between dropoff and pickup
hours = delta.total_seconds() / 3600
````

Each approach has trade-offs:
- unix_timestamp gives per-row exact hours including minutes and seconds.
- datediff provides a quick day-based delta (multiplying by 24 to get hours) but loses sub-day precision.
- Python-side timedelta is useful when you're operating outside Spark/after collecting, but it requires moving data to the driver.
