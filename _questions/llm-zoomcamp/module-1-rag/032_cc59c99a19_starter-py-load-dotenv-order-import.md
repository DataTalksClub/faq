---
id: cc59c99a19
question: Why does `starter.py` fail if you don’t call `load_dotenv()` before importing
  it?
sort_order: 32
---

`starter.py` runs module-level code at import time: it creates the OpenAI client immediately (e.g., `client = OpenAI()`). If the API key isn’t already present in your process environment (because the notebook/script hasn’t loaded your `.env` file yet), importing `starter.py` fails with an authentication error.

Fix:
- Call `load_dotenv()` before importing `starter`.

Example order:
```python
from dotenv import load_dotenv
load_dotenv()          # must run first

import starter         # now client = OpenAI() can read OPENAI_API_KEY
```

For the monitoring homework, this same “order matters” idea also applies to OpenTelemetry: the homework asks you to register your `TracerProvider` before importing `starter`. So the safe top-of-notebook/script order is:
1) set up the tracer provider, 2) call `load_dotenv()`, 3) then import `starter`.