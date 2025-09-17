---
id: 1da0437718
question: Homework - how to convert the time difference of two timestamps to hours
section: Module 5: pyspark
course: data-engineering-zoomcamp
sort_order: 3800
---

Pyspark converts the difference of two TimestampType values to Python's native datetime.timedelta object. The timedelta object only stores the duration in terms of days, seconds, and microseconds. Each of the three units of time must be manually converted into hours in order to express the total duration between the two timestamps using only hours.

Another way for achieving this is using the datediff (sql function). It receives this parameters

Upper Date: the closest date you have. For example dropoff_datetime

Lower Date: the farthest date you have.  For example pickup_datetime

And the result is returned in terms of days, so you could multiply the result for 24 in order to get the hours.

