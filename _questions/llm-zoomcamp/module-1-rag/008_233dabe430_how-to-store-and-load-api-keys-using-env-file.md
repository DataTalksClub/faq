---
id: 233dabe430
question: How to store and load API keys using .env file
sort_order: 8
---

Store API keys in a `.env` file and load them with `python-dotenv`, as recommended in the course.

Add `.env` to `.gitignore` so keys are never committed:

```gitignore
.env
```

Create a `.env` file:

```bash
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk_...
GEMINI_API_KEY=...
```

Install `python-dotenv` if needed:

```bash
pip install python-dotenv
```

Load the keys in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
```
