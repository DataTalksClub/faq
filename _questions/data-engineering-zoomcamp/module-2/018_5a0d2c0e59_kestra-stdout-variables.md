---
id: 5a0d2c0e59
question: Why doesn’t Kestra automatically convert printed task outputs into variables?
sort_order: 18
---

Kestra distinguishes between execution logs and structured outputs. Values printed to stdout are treated as logs for observability, not as structured data. Explicit output definitions are required to persist or reuse values across tasks.