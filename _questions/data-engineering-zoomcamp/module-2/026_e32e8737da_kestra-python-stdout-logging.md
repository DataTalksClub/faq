---
id: e32e8737da
question: How to fix Python logs shown as Kestra error messages?
sort_order: 26
---

The issue comes down to how Unix processes produce output and how Kestra interprets it:

1. Python's `logging` module writes to `stderr` by default. If you, for instance, call `logging.basicConfig()` without specifying a `stream` argument, the root handler sends basically everything to `stderr`.

2. Kestra maps the two standard streams to its own log levels. Anything the container writes to `stdout` becomes a Kestra **DEBUG** entry and anything written on `stderr` becomes **ERROR**. There is no middle ground.

The fix

Good news is that the fix is simple: redirect Python logging to `stdout`:

```python
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout,
)
```

That single `stream=sys.stdout` argument is enough. After the change, your informational messages will show up as **DEBUG** in Kestra.