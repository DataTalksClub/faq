---
id: 4a2c64c6e7
question: How can I inspect an unfamiliar LLM API response to find tool calls, token
  usage, or other fields?
sort_order: 32
---

If you’re adapting the course code to another provider or API style, first inspect the complete response object—different APIs (e.g., Responses API vs Chat Completions vs provider SDKs) expose different field names, so the fastest path is to print the whole structure.

If `response` is a Pydantic model, convert it to a dictionary with `response.model_dump()`. In a notebook, you can display it as an expandable JSON tree:

```python
from IPython.display import JSON

# Assuming `response` is the full object returned by the API
JSON(response.model_dump())
```

In a script/terminal, print formatted JSON:

```python
import json

print(json.dumps(response.model_dump(), indent=2))
```

Then search the printed output for the fields you care about, such as:
- tool/function calling results (often under names like `tool_calls`, `tools`, or provider-specific structures)
- token usage (often under `usage`, with subfields like `prompt_tokens`, `completion_tokens`, `total_tokens`)
- the actual generated text (often under `choices` / `message` / `content` or provider-specific equivalents)

Once you identify the corresponding keys for your provider, update the course’s parsing code to read those fields instead of the OpenAI-specific ones (and avoid assuming tokenization fields are consistent across providers).