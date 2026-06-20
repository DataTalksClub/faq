---
id: cfb07a27d5
question: 'OpenRouter: Error code 402 when calling responses.create (max_output_tokens)'
sort_order: 2
---

OpenRouter can return APIStatusError with code 402 when responses.create() is called without a reasonable max_output_tokens limit. This happens because OpenRouter bills/limits checks against the maximum possible output (which can be very large, around 65536 tokens), so a free or low-limit key can be rejected before the model runs. This is different from a direct OpenAI endpoint (which typically returns 429 for insufficient quota).

Fix

Pass a lower limit in your responses.create() call:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()  # uses OPENAI_API_KEY and OPENAI_BASE_URL from .env

response = client.responses.create(
    model=os.environ["OPENAI_MODEL"],
    input=message_history,
    max_output_tokens=1024,
)
```

For Module 1 homework with rag_helper.py, add the same parameter in the ``llm()`` method.

```python
response = client.responses.create(
    model=os.environ["OPENAI_MODEL"],
    input=message_history,
    max_output_tokens=1024,
)
```

For Module 1 homework Q6 with ToyAIKit:

```python
from toyaikit.llm import OpenAIClient

llm_client = OpenAIClient(
    model=os.environ["OPENAI_MODEL"],
    extra_kwargs={"max_output_tokens": 1024},
)
```

1024 is enough for homework answers; you can raise it later if needed.

If it still fails

1) Confirm your `.env` points at OpenRouter:

```env
OPENAI_API_KEY=sk-or-v1-...
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=openai/gpt-oss-120b:free
```

2) Check your OpenRouter key limit and remaining credits at https://openrouter.ai/settings/keys

3) Prefer a pinned model (for example `openai/gpt-oss-120b:free`) instead of `openrouter/free`, which can route to models with different limits.

Note: This behavior is different from OpenAI’s typical 429 handling for insufficient quota. If you still encounter issues after these steps, double-check the model and endpoint configuration to ensure the key is valid and has sufficient credits.