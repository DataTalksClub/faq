---
id: b7e9d1c052
question: How do I avoid backpressure in a Flink streaming job?
sort_order: 31
---

Backpressure occurs when Flink processes data slower than the upstream source produces it. This causes growing buffers, increased memory usage, and can eventually slow down or crash the job.

How to mitigate it:

- Increase consumer parallelism so more tasks process records in parallel.
- Increase the number of partitions on the source topic so the additional Flink consumers actually have separate partitions to read from.
- Watch Flink's metrics (the "Backpressure" tab in the Web UI, or the `inputRate`/`outputRate` task metrics) to confirm where the bottleneck is.

Setting parallelism in PyFlink:

```python
env.set_parallelism(4)
```

Increase parallelism gradually and re-check metrics — making it too large just shifts the bottleneck somewhere else (network, sink, etc.).
