---
id: b391cb9b0b
question: How do I fix GroqError or model_decommissioned errors when my Groq model stops working?
sort_order: 36
---

If you see `GroqError` / `model_decommissioned`, your Groq model ID was retired. As of August 2026, `llama-3.3-70b-versatile` and `qwen/qwen3-32b` were retired by Groq — switch to a currently supported model and update reasoning effort:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    model="openai/gpt-oss-120b",
    input="Hello",
    reasoning={"effort": "low"},  # gpt-oss accepts only "low", "medium", or "high"
)

print(response.output_text)
```

If your code uses `reasoning_effort="none"` (Chat Completions style, valid for older Qwen models), the Responses API equivalent is `reasoning={"effort": "low"}` — `"none"` is rejected for `gpt-oss-120b` and you get a validation error on every request.

Check [Groq deprecations](https://console.groq.com/docs/deprecations) for current model status, [Groq reasoning docs](https://console.groq.com/docs/reasoning) for supported effort values, and [Groq Responses API docs](https://console.groq.com/docs/responses-api) for the request shape.
