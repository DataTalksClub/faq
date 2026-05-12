---
id: 1b08427cd4
question: No module named ‘ping’?
sort_order: 59
---

When you encounter the error stating that there is no module named 'ping', it means the 'ping' module is not found in your Python environment.

To fix this, you can import the 'ping' function directly from the specific file where it is defined using:

```python
from [file name] import ping
```

Replace `[file name]` with the actual file name where the 'ping' function is located.