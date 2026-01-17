---
id: 5bf119a791
question: What does concurrency mean in Kestra, and how does it work?
sort_order: 1
---

In Kestra, concurrency means controlling how many executions of the same flow can run at the same time. It is used to prevent problems such as duplicate processing, data corruption, or excessive resource usage when a flow is triggered multiple times.

Concurrency Limit
```yaml
concurrency:
  limit: 1
```

This configuration means that only one execution of the flow can run at a time. If the flow is already running and another execution is triggered, Kestra applies the concurrency behavior defined below.

Concurrency Behavior Options
