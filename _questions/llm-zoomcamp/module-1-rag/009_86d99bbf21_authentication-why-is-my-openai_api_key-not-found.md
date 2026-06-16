---
id: 86d99bbf21
question: 'Authentication: Why is my OPENAI_API_KEY not found in the Jupyter notebook?'
sort_order: 7
---



Make sure you installed and used `python-dotenv`.

```bash
pip install python-dotenv
```

Then load the `.env` file in the notebook before creating the OpenAI client:

```python
from dotenv import load_dotenv

load_dotenv()
```

Also check that the variable name in `.env` is exactly `OPENAI_API_KEY`.
