---
id: 0bed1f48da
question: dotenv is not recognized. What should I install?
sort_order: 25
---

Install `python-dotenv`:

```bash
uv add python-dotenv
```

Then import and use it in Python:

```python
from dotenv import load_dotenv

load_dotenv()
```

The package is documented here: [python-dotenv](https://pypi.org/project/python-dotenv/).
