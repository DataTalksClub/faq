---
id: 29e617a947
question: Why does the tumbling window job run successfully but the PostgreSQL sink
  table returns no rows when queried?
sort_order: 28
---

Flink streaming jobs emit results only after the window closes. With event-time processing and watermarks, the window will not close until the watermark passes the window end. If you query the PostgreSQL table too early, it may still be empty even though the job is running correctly. Let the job run for a short time so the watermark advances and the window results are written to the sink table.
