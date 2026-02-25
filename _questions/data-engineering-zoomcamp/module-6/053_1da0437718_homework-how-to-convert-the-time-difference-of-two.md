---
id: 1da0437718
question: 'Homework: how to convert the time difference of two timestamps to hours'
sort_order: 53
---

Pyspark converts the difference of two `TimestampType` values to Python's native `datetime.timedelta` object. The `timedelta` object stores the duration in terms of days, seconds, and microseconds. Each of these units must be manually converted into hours to express the total duration between the two timestamps using only hours.

Another method to achieve this is using the `datediff` SQL function. It requires the following parameters:

- **Upper Date**: The closer date, e.g., `dropoff_datetime`.
- **Lower Date**: The farther date, e.g., `pickup_datetime`.

The result is returned in days, so you can multiply the result by 24 to get the duration in hours.