---
id: e08b9c753f
question: PyFlink session window job fails with 'please declare primary key for sink
  table when query contains update/delete record' error
sort_order: 27
---

Session window aggregations produce updates while the session is still open. The JDBC sink needs a primary key so it knows which row should be updated in the table. Without a primary key, Flink cannot apply the updates and the job fails. Define a primary key in the sink table using the window boundaries and the grouping key (for example window_start, window_end, and PULocationID).
